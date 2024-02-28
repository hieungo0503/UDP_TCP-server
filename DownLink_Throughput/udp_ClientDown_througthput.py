import serial
import time

def send_at_command(serial_port, command):
    serial_port.write(command.encode() + b'\r\n')
    time.sleep(0.1)  # Wait for response

def read_response(serial_port):
    response = b''
    while serial_port.in_waiting:
        response += serial_port.read(serial_port.in_waiting)
    return response.decode()
def Rc_byteAtComma(Comma, Response):
    # time.sleep(0.2)
    dataLen = Response.strip().split(",")
    if len(dataLen) > Comma :  # Check if the element exists and is non-empty and dataLen[Comma].strip()
        return int(dataLen[Comma])
    else:
        return 0  # Or handle the error in a way appropriate to your application

# Replace 'COM35' with your serial port name and 115200 with your baud rate
ser = serial.Serial('COM35', 115200, timeout=1)

# Send AT commands and read responses
total_bytes_received = 0
timeOut = 4 
duration_seconds = 0

CheckOut = 1
while CheckOut <= 5:      # number of tests
    total_bytes_received = 0
    start_time = None
    time_Counter = None
    command = "AT+CSOSEND=0,0,\"000\""  #Replace your AT command Sending data
    send_at_command(ser, command)
    while True:
        response = read_response(ser)
        if '+CSONMI:' in response:      #Replace your Receive recognize  
            time_Counter = time.time()
            if start_time == None:  
                start_time = time.time()
                print(f"CheckOut {CheckOut} is being process")
                print("=======================================")
            bytesRc = Rc_byteAtComma(1,response)
            # print('+CSONMI:' , bytesRc)
            total_bytes_received += bytesRc
        if start_time != None:
            if(time.time()- time_Counter >= timeOut):
                print("total byte rc: ", total_bytes_received)
                duration_seconds = time.time() - start_time - timeOut
                break   

    data_rate = total_bytes_received * 8 /  duration_seconds  # Convert bytes to bits
    data_rate_kbps = data_rate / 1000  # Convert bits per second to kilobits per second
    print(f"Total bytes received: {total_bytes_received} bytes")
    print(f"Duration: {duration_seconds:.2f} seconds")
    print(f"UDP receiving data rate: {data_rate_kbps:.2f} kbps")
    print("=======================================")
    CheckOut +=1

