
import socket
import time
 

localIP     = "192.168.1.99" 

localPort   = 23152

bufferSize  = 1024

 

packet_size = 512
bytesToSend         = '0' * packet_size
# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")

    

# Listen for incoming datagrams
duration = 60
while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]
    
    clientMsg = message.decode()
    if 's' in clientMsg:
        parts = clientMsg.split('s')
        duration = int(parts[0])
        bytesToSend = int(parts[1][:-2]) * '0'

    # print(duration,bytesToSend)

    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP) 


# Sending a reply to client
    start_time = time.time()

# Send packets continuously for the specified duration
    while time.time() - start_time < duration:
        UDPServerSocket.sendto(bytesToSend.encode('utf-8'), address)
        time.sleep(0.02)
    
    print(f"send Done in {duration}s and {len(bytesToSend)} bytes")
