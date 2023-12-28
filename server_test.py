import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.1.226', 20002)
print('starting up on addr: ', server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    # try:
    print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(1024)
        # print('received: ', data)
        data_parsed = data.decode('utf-8').strip("*#\n")
        # print(data_parsed.strip("*#\n"))
        format_str = "header,manu_code,imei,time,type,data"
        keys = format_str.split(",")
        values = data_parsed.split(",", 5)
        cmd_dict = dict(zip(keys, values))
        print(cmd_dict)
        if data:
            alarm = "FFFF" + "*CMDS,OM,862205053707503,000000000000,L0,0,0,1689586634#\n".encode("utf-8").hex()
            print(alarm)
            alarm = bytes.fromhex(alarm)
            print(alarm)
            print('sending data back to the client')
            connection.sendall(alarm)
        else:
            print('no more data from', client_address)
            break
