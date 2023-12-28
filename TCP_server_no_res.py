import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, client_address, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        print("New connection added: ", client_address)

    def run(self):
        message = ''
        while True:
            data = self.client_socket.recv(1024)
            message = data.decode()
            if message=='bye':
              break
            print("from client", message)
            # self.client_socket.sendall("ACK".encode())
        print("Client at ", client_address , " disconnected...")

host = "192.168.1.226"
port = 23030

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))

print("TCP server waiting for client on port", port)

while True:
    server_socket.listen(1)
    client_sock, client_address = server_socket.accept()
    new_thread = ClientThread(client_address, client_sock)
    new_thread.start()
