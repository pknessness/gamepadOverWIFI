import hid
import time# wait
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d

import sys
 
import pygame
from pygame.locals import *
 
pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
fps = 60
fpsClock = pygame.time.Clock()

for device in hid.enumerate():
    print(f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}")

gamepad = hid.device()
gamepad.open(0x045e,0x028e)
#gamepad.open(0x1949,0x041a)

print("\n\nYEET\n\n")

print("Manufacturer: %s" % gamepad.get_manufacturer_string())
print("Product: %s" % gamepad.get_product_string())
print("Serial No: %s" % gamepad.get_serial_number_string())

gamepad.set_nonblocking(True)

time.sleep(0.05)
print("begin?")
while True:
    report = gamepad.read(64)
    if report:
        screen.fill((0, 0, 0))
        print(".",report)
        for i in range(len(report)):
            pygame.draw.rect(screen,(100,0,250),Rect((20 * i),10,20,report[i]))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
  
    # Update.
  
    # Draw.
  
    pygame.display.flip()
    fpsClock.tick(fps)