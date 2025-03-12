#! /usr/bin/python3
'''
'''
import socket
import sys
def main():
# ups msg/cnt counter_val ip
# ups cnt 100 127.0.0.1
    msg_cnt = 0
    msg_cnt_interval = 10
    print_msg = 1
    if len(sys.argv) > 3:
        server_address = (sys.argv[1], 8080)
    else:
        server_address = ('127.0.0.1', 8080)

    if len(sys.argv) >= 2:
        if (sys.argv[1] == "msg"):
            print("print msg")
        else:
            print_msg = 0
            print("print cnt")
    else:
        print("arg2 is null")
    if len(sys.argv) == 3:
        msg_cnt_interval = int(sys.argv[2])

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(server_address)
    while True:
        data, client_address = server_socket.recvfrom(4096)
        if data:
            if print_msg == 1:
                print("Wait for message: ")
                print ("\n\t Got the data: \n")
                str_message = data.decode('utf-8')
                print(str_message)
            else:
                msg_cnt = msg_cnt + 1
                if msg_cnt % msg_cnt_interval == 0:
                    print(msg_cnt)
                    print("===\n")
    server_socket.close()

if __name__ == "__main__":
    main()

