import socket
import time

def udp_server(host, port, timeOut):
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP server listening on {host}:{port}")
    while True:
        total_bytes_received = 0
        start_time = None
        while True:
           try:
                server_socket.settimeout(timeOut)
                data, address = server_socket.recvfrom(1024)
                if data:
                    if start_time is None:
                        start_time = time.time()
                        print("Client IP Address:{}".format(address))
                    total_bytes_received += len(data)
           except socket.timeout:
                # Break out of the inner loop if timeout occurs
                break
        if start_time != None:
        # Calculate data rate
            end_time = time.time()
            duration_seconds = end_time - start_time - timeOut
            data_rate = total_bytes_received * 8 / duration_seconds  # Convert bytes to bits
            data_rate_kbps = data_rate / 1000  # Convert bits per second to kilobits per second

            print(f"Total bytes received: {total_bytes_received} bytes")
            print(f"Duration: {duration_seconds:.2f} seconds")
            print(f"UDP receiving data rate: {data_rate_kbps:.2f} kbps")
            message_send = f"Bytes Receice: {total_bytes_received} bytes; Time: {duration_seconds:.2f} s; Data_Rate: {data_rate_kbps:.2f} kbps"
            server_socket.sendto(message_send.encode('utf-8'),address)

def main():
    host = "192.168.1.99"  # Listen on localhost
    port = 23152           # Choose a port number        
    TimeOut = 10
    udp_server(host, port, TimeOut)

if __name__ == "__main__":  
    main()
