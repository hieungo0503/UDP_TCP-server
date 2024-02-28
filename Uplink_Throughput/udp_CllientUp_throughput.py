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
        return dataLen[Comma]
    else:
        return 0  # Or handle the error in a way appropriate to your application

# Replace 'COM35' with your serial port name and 115200 with your baud rate
ser = serial.Serial('COM35', 115200, timeout=1)

duration_seconds = 60
packet_size = 512
bytesToSend        = '0' * packet_size
CheckOut = 1

while CheckOut <= 5:      # number of tests
    start_time = time.time()
    print(f"CheckOut {CheckOut} is being process")
    print("================================")
    while time.time() - start_time < duration_seconds:
        command = "AT+CSOSEND=0,0,\"{}\"".format(bytesToSend)  #Replace your AT command Sending data
        # print(command)
        send_at_command(ser, command)
        response = read_response(ser)
        # print(response)
    while True:
        response = read_response(ser)
        if '+CSONMI:' in response:
            time_Counter = time.time()
            message = Rc_byteAtComma(2,response)
            print(F"Respond From Server: {message}")
            break 
    CheckOut += 1
    # while True:
    #     response = read_response(ser)
    #     if '+CSONMI:' in response:      #Replace your Receive recognize  
    #         time_Counter = time.time()
    #         if start_time == None:  
    #             start_time = time.time()
    #             print(f"CheckOut {CheckOut} is being process")
    #             print("=======================================")
    #     if start_time != None:
    #         if(time.time()- time_Counter >= timeOut):
    #             print("total byte rc: ", total_bytes_received)
    #             duration_seconds = time.time() - start_time - timeOut
    #             break   

   

