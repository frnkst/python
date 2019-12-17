# SSH honeypot that sends a telegram message to a channel every time
# somebody tries to log in. The ip address will be reported along with
# tried the username and password.
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

config = configparser.ConfigParser()
config.read(os.path.join(sys.path[0], 'telegram.ini'))
telegram = config['telegram']

# generate keys with 'ssh-keygen -t rsa -f server.key'
HOST_KEY = paramiko.RSAKey(filename='server.key')
SSH_PORT = 22
LOGFILE = 'login_attempts.txt'
LOGFILE_LOCK = threading.Lock()
IP_ADDRESSES_LOCK = threading.Lock()

unique_ip_addresses = []


def send_telegram_message(text):
    token = telegram['bot_token']
    id = telegram['chat_id']
    url = ("https://api.telegram.org/%s/sendMessage?chat_id=%s&text=%s" % (token, id, text))
    requests.get(url)


class SSHServerHandler(paramiko.ServerInterface):
    def __init__(self, ip_address):
        self.ip_address = ip_address
        if ip_address not in unique_ip_addresses:
            unique_ip_addresses.append(ip_address)
            send_telegram_message("New ip address seen: https://whatismyipaddress.com/ip/" + ip_address)

    def check_auth_password(self, username, password):
        LOGFILE_LOCK.acquire()
        try:
            logfile_handle = open(LOGFILE, "a")
            text = "%s %s:%s\n" % (self.ip_address, username, password)
            logfile_handle.write(text)
            send_telegram_message(text)
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
