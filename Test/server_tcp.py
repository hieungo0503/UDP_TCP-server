import socket
import threading

def handle_client(client_socket, client_address):
    # Receive data from the client
    data = client_socket.recv(1024)
    print(f"Received data from {client_address}: {data}")
    # Send a response to the client
    response = b"Hello from the server!"
    client_socket.send(response)
    # Close the client socket
    client_socket.close()

def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to a specific address and port
    server_address = ('0.0.0.0', 12345)
    server_socket.bind(server_address)
    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {server_address}")
    while True:
        # Wait for a client to connect
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == '__main__':
    start_server()

