import socket
import os
import sys
 
# 创建一个 Unix socket
server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
 
# 获取一个临时的 socket 文件名
#socket_file = '/tmp/test_socket-%d' % os.getpid()
socket_file = '/tmp/test_unix_socket'
 
# remove the file if it is exist
if os.path.exists(socket_file):
    os.remove(socket_file)
    print(f" file {socket_file} is removed")

# 绑定到 socket 文件
server.bind(socket_file)
 
# 监听客户端连接
server.listen(5)
 
while True:
    # 接受客户端连接
    connection, client_address = server.accept()
    
    try:
        while True:
            data = connection.recv(4096)
            if data:
                print("收到: %s" % data.decode('utf-8'))
                connection.sendall(data)
            else:
                break
    except socket.error as e:
        print(e)
    
    connection.close()
