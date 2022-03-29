import pygame
from pygame.locals import *

pygame.display.init()
pygame.joystick.init()
controller = pygame.joystick.Joystick(0)
controller.init()
axis = {}
button = {}

# these are the identifiers for the PS4's accelerometers
AXIS_X = 16
AXIS_Y = 17

# variables we'll store the rotations in, initialised to zero
rot_x = 0.0
rot_y = 0.0

# main loop
while True:

    # copy rot_x/rot_y into axis[] in case we don't read any
    axis[AXIS_X] = rot_x
    axis[AXIS_Y] = rot_y

    # retrieve any events ...
    for event in pygame.event.get():

        if event.type == pygame.JOYAXISMOTION:
            axis[event.axis] = round(event.value,2)
        elif event.type == pygame.JOYBUTTONDOWN:
            button[event.button] = True
        elif event.type == pygame.JOYBUTTONUP:
            button[event.button] = False

    rot_x = axis[AXIS_X]
    rot_y = axis[AXIS_Y]            

    # do something with this ...
    print("X?:",rot_x,"\tY?:",rot_y)