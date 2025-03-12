import socket
import os
 
# 创建一个 Unix socket
client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
 
# 连接到服务器的 socket 文件
#socket_file = '/tmp/test_socket-%d' % os.getpid()
socket_file = '/tmp/test_unix_socket'
client.connect(socket_file)
 
# 发送数据
client.sendall(b'Hello, world')
 
# 接收响应
data = client.recv(16)
print('收到: %s' % data.decode('utf-8'))
 
# 关闭连接
client.close()
