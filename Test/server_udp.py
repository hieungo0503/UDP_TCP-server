import socket
import threading

def handle_client(client_socket, client_address):
    while True:
        data, addr = client_socket.recvfrom(1024)
        if not data:
            break
        print(f"Received data from {client_address}: {data}")
        data = "FEFEFEFE6808000508032268110433333433EC16"
        # client_socket.sendto(bytes.fromhex(data), client_address)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 20001))

    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received connection from {addr}")
        thread = threading.Thread(target=handle_client, args=(server_socket, addr))
        thread.start()

if __name__ == '__main__':
    start_server()

