#! /usr/bin/python3
'''
'''
import socket
import sys

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if len(sys.argv) > 1:
        server_address = (sys.argv[1], 8080)
    else:
        server_address = ('127.0.0.1', 8080)

    server_socket.bind(server_address)
    cur_cnt = 0
    new_inc_cnt = 0
    print("Wait for message: ")
    while True:
        data, client_address = server_socket.recvfrom(46080)
        if data:
            cur_cnt = cur_cnt + 1
            new_inc_cnt = new_inc_cnt + 1
            if (new_inc_cnt > 10000):
                new_inc_cnt = 0
                print (f'\n\t Got the data counter: <{cur_cnt}>\n')
    server_socket.close()

if __name__ == "__main__":
    main()

