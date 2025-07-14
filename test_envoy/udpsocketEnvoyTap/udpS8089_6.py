#! /usr/bin/python3
'''
'''
import socket
import sys

def main():
    server_socket = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    if len(sys.argv) > 1:
        server_address = (sys.argv[1], 8089)
    else:
        server_address = ('::1', 8089)

    server_socket.bind(server_address)
    while True:
        print("Wait for message: ")
        data, client_address = server_socket.recvfrom(30720)
        if data:
            print ("\n\t Got the data: \n")
            str_message = data.decode('utf-8')
            print(str_message)
    server_socket.close()

if __name__ == "__main__":
    main()

