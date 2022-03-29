from re import I
import numpy as np

#def bitfield(n):
#    return [int(digit) for digit in bin(n)[2:]]

def int8_to_byte_array(n):
    return [int(digit) for digit in np.binary_repr(n,width=8)]

def int8_to_byte_array(n, num):
    return [int(digit) for digit in np.binary_repr(n,width=num)]

vals = [0,1,0,0,0,0,0,1,0,0,0,0,0,0,-128,127,127,127,127,127] 
# A B X Y D-UP D-DOWN D-LEFT D-RIGHT L1 L2 Back Start L-THUMB R-THUMB L-Y L-X R-Y R-X L-T R-T

def byte_to_int8(n):
    o = 0
    for i in n:
        o = (o << 1) + i
    return o

numB = 14
numA = 6

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
        x = int8_to_byte_array(values[i],8)
        #x = [int(digit) for digit in np.binary_repr(values[i],width=8)]
        if(i < numButtons):
            byteString = (byteString << 1) + x[7]
            #print(int8_to_byte_array(byteString,64))
        else:
            for y in x:
                byteString = (byteString << 1) + y
            #print(int8_to_byte_array(byteString,64))
    return [byte_to_int8(int8_to_byte_array(byteString,64)[8*d:8*d+8]) for d in range(8)]



#for i in range(numAxes):
#    byteS += "."
#    byteString = (byteString << (numAxes - i)) + ((values[i + numButtons] >> (7 - i)) & 1)
#    byteS += str((values[i + numButtons] >> (7 - i)) & 1)
#    print(((values[i + numButtons] >> (7 - i)) & 1))
byt = bytes(gamepadToBytes(vals,numB,numA))
itn = gamepadToInt(vals,numB,numA)
print(byt)
#print(int8_to_byte_array(byt,64))
print("-")
print(itn)
print(int8_to_byte_array(itn,64))
print("-")
print(int.from_bytes(byt,byteorder='big',signed=False))
print(int8_to_byte_array(int.from_bytes(byt,byteorder='big',signed=False),64))