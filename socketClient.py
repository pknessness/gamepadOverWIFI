# echo-client.py

import socket
import numpy as np
from xboxAPI import *

def int8_to_byte_array(n, num):
    return [int(digit) for digit in np.binary_repr(n,width=num)]

def byte_to_int8(n):
    o = 0
    for i in n:
        o = (o << 1) + i
    return o

def gamepadToInt(values, numButtons, numAxes):
    byteString = 0

    for i in range(numButtons + numAxes):
        x = int8_to_byte_array(values[i],8)
        #x = [int(digit) for digit in np.binary_repr(values[i],width=8)]
        if(i < numButtons):
            byteString = (byteString << 1) + x[7]
            #print(int8_to_byte_array(byteString,64))
        else:
            for y in x:
                byteString = (byteString << 1) + y
            #print(int8_to_byte_array(byteString,64))
    return byteString

def gamepadToBytes(values, numButtons, numAxes):
    byteString = 0

    for i in range(numButtons + numAxes):
        if(i < numButtons):
            x = int8_to_byte_array(values[i],8)
        else:
            x = int8_to_byte_array(int(values[i] * 128),8)
        #x = [int(digit) for digit in np.binary_repr(values[i],width=8)]
        if(i < numButtons):
            byteString = (byteString << 1) + x[7]
            #print(int8_to_byte_array(byteString,64))
        else:
            for y in x:
                byteString = (byteString << 1) + y
            #print(int8_to_byte_array(byteString,64))
    return [byte_to_int8(int8_to_byte_array(byteString,64)[8*d:8*d+8]) for d in range(8)]

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

#with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#    s.connect((HOST, PORT))
#    s.sendall(b"Hello, world")
#    data = s.recv(1024)

#print(f"Received {data!r}")

gamepad = XboxController()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while(1): 
        print(gamepad.read())
        s.sendall(bytes(gamepadToBytes(gamepad.read(),14,6)))
        data = s.recv(1024)


    
