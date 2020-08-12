# Source: https://github.com/internetwache/SSH-Honeypot/blob/master/honeypot.py

import socket
import sys
import _thread
import paramiko
import threading

# generate keys with 'ssh-keygen -t rsa -f server.key'
HOST_KEY = paramiko.RSAKey(filename='server.key')
SSH_PORT = 22
LOGFILE = 'login_attempts.txt'
IP_ADDRESSES_FILE = 'ip_addresses.txt'
LOGFILE_LOCK = threading.Lock()
IP_ADDRESSES_LOCK = threading.Lock()


class SSHServerHandler(paramiko.ServerInterface):
    def check_auth_password (self, username, password):

        LOGFILE_LOCK.acquire()
        try:
            logfile_handle = open(LOGFILE, "a")
            logfile_handle.write(username + ":" + password + "\n")
            logfile_handle.close()
        finally:
            LOGFILE_LOCK.release()
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return 'password'


def handle_connection(client, client_address):
    transport = paramiko.Transport(client)
    transport.add_server_key(HOST_KEY)

    server_handler = SSHServerHandler()

    transport.start_server(server=server_handler)

    channel = transport.accept(1)
    if channel is not None:
        channel.close()


def log_ip_addresses(client_address):
    IP_ADDRESSES_LOCK.acquire()
    try:
        ip_addresses_handle = open(IP_ADDRESSES_FILE, "a")
        ip_addresses_handle.write(client_address[0] + "\n")
        ip_addresses_handle.close()
    finally:
        IP_ADDRESSES_LOCK.release()


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
                log_ip_addresses(client_address)
                _thread.start_new_thread(handle_connection, (client_socket, client_address))
            except Exception as e:
                print("ERROR: Client handling")
                print(e)

    except Exception as e:
        print("ERROR: Failed to create socket")
        print(e)
        sys.exit(1)


main()
