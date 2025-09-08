import socket

def udp_client(server_host="127.0.0.1", server_port=9999, message="Hello from client"):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # If you want conntrack to create an entry without connect(),
    # just use sendto()
    sock.sendto(message.encode(), (server_host, server_port))
    print(f"Sent: {message}")

    # receive response (optional)
    data, addr = sock.recvfrom(1024)
    print(f"Received from {addr}: {data.decode()}")

if __name__ == "__main__":
    udp_client()

