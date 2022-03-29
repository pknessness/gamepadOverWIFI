# echo-server.py

import socket
import keyboard
import numpy as np
from xboxAPI import *

def int8_to_byte_array(n, num):
    return [int(digit) for digit in np.binary_repr(n,width=num)]

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
while 1:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                try:
                    data = conn.recv(1024)
                    if(not str(data) == 'b\'\''):
                        #print(data)
                        print("Recieved:",int8_to_byte_array(int.from_bytes(data,byteorder='big',signed=False),64))
                    if(keyboard.is_pressed('end')):
                        break
                    conn.sendall(b'Recieved')
                except:
                    break
                