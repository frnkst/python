# SSH honeypot that sends a telegram message with a summary of
# all IP's that tried to connect within a certain time frame and
# the last 20 login attempts.
#
# Create an telegram.ini file in the same folder as the script
# and add the following contents (replace <bot-token> and <chat-id>
# with actual real values
#
# Filename: telegram.ini
# [telegram]
# bot_token = <bot-token>
# chat_id = <chat-id>
import socket
import sys
import _thread
import paramiko
import threading
import configparser
import os
import requests
import datetime

INTERVAL = 3 * 60
unique_ip_addresses = []
login_attempts = []

# generate keys with 'ssh-keygen -t rsa -f server.key'
HOST_KEY = paramiko.RSAKey(filename='server.key')
SSH_PORT = 22
LOGFILE = 'login_attempts.txt'
LOGFILE_LOCK = threading.Lock()
IP_ADDRESSES_LOCK = threading.Lock()

config = configparser.ConfigParser()
config.read(os.path.join(sys.path[0], 'telegram.ini'))
telegram = config['telegram']

start_time = datetime.datetime.now()


def time_to_send_summary():
    if (datetime.datetime.now() - start_time).total_seconds() / 60 >= INTERVAL:
        return True


def get_summary():
    start = start_time.time().strftime("%H:%M:%S")
    end = datetime.datetime.now().time().strftime("%H:%M:%S")
    title = ("Activity between %s and %s \n\n" % (start, end))
    body = ("%s unique ip addresses tried to connect: \n" % len(unique_ip_addresses))
    body = body + "\n".join(unique_ip_addresses)
    body = body + "\n \nThe last connection attempts were: \n"

    if len(login_attempts) > 30:
        body = body + "".join(login_attempts[-30:])
    else:
        body = body + "".join(login_attempts)
    return title + body


def reset_time_and_values():
    global login_attempts, unique_ip_addresses, start_time
    login_attempts = []
    unique_ip_addresses = []
    start_time = datetime.datetime.now()


def send_telegram_message():
    if time_to_send_summary() is True:
        text = get_summary()
        token = telegram['bot_token']
        id = telegram['chat_id']
        url = ("https://api.telegram.org/%s/sendMessage?chat_id=%s&text=%s" % (token, id, get_summary()))
        requests.get(url)
        reset_time_and_values()



class SSHServerHandler(paramiko.ServerInterface):
    def __init__(self, ip_address):
        self.ip_address = ip_address
        if ip_address not in unique_ip_addresses:
            unique_ip_addresses.append(ip_address)

    def check_auth_password(self, username, password):
        LOGFILE_LOCK.acquire()
        try:
            logfile_handle = open(LOGFILE, "a")
            text = "%s %s:%s\n" % (self.ip_address, username, password)
            login_attempts.append(text)
            send_telegram_message()
            logfile_handle.close()
        finally:
            LOGFILE_LOCK.release()
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return 'password'


def handle_connection(client, client_address):
    transport = paramiko.Transport(client)
    transport.add_server_key(HOST_KEY)

    server_handler = SSHServerHandler(client_address[0])

    transport.start_server(server=server_handler)

    channel = transport.accept(1)
    if channel is not None:
        channel.close()


def main():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(('', SSH_PORT))
        server_socket.listen(100)

        paramiko.util.log_to_file('paramiko.log')

        while True:
            try:
                client_socket, client_address = server_socket.accept()
                _thread.start_new_thread(handle_connection, (client_socket, client_address))
            except Exception as e:
                print("ERROR: Client handling")
                print(e)

    except Exception as e:
        print("ERROR: Failed to create socket")
        print(e)
        sys.exit(1)


main()
