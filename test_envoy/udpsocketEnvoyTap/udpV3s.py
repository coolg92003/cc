import socket

def udp_server(host="0.0.0.0", port=9999):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print(f"UDP server listening on {host}:{port}")

    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Received from {addr}: {data.decode()}")
        # echo back
        sock.sendto(b"Echo: " + data, addr)

if __name__ == "__main__":
    udp_server()

