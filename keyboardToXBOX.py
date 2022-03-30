import vgamepad as vg
import keyboard as k

gamepad = vg.VX360Gamepad()

buttonMap = {
    "t":vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
    "g":vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
    "f":vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
    "h":vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
    "y":vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
    "r":vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK,
    "[":vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
    "]":vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB,
    "e":vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
    "u":vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
    "space":vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE,
    "k":vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
    "l":vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
    "j":vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
    "i":vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
}

QUIT_KEY = "end"

analogMap = {
    "w":"lY+1", #LEFT STICK - UP
    "s":"lY-1", #LEFT STICK - DOWN
    "a":"lX-1", #LEFT STICK - LEFT
    "d":"lX+1", #LEFT STICK - RIGHT
    "up":"rY+1", #RIGHT STICK - UP
    "down":"rY-1", #RIGHT STICK - DOWN
    "left":"rX-1", #RIGHT STICK - LEFT
    "right":"rX+1", #RIGHT STICK - RIGHT
    "q":"TL+1", #LEFT TRIGGER
    "o":"TR+1", #RIGHT TRIGGER
}
l = [0,0]
r = [0,0]
while(1):

    l = [0,0]
    r = [0,0]
    gamepad.left_trigger_float(0)
    gamepad.right_trigger_float(0)

    for i in buttonMap:
        if(k.is_pressed(i)):
            gamepad.press_button(buttonMap[i])
            print(i, " is pressed")
        else:
            gamepad.release_button(buttonMap[i])

    for i in analogMap:
        if(k.is_pressed(i)):

            print(i, " is pressed")
            val = int(analogMap[i][2:4])
            #print(analogMap[i][0:2],val)

            if(analogMap[i][0:2] == "TL"):
                gamepad.left_trigger_float(1)
            if(analogMap[i][0:2] == "TR"):
                gamepad.right_trigger_float(1)
            if(analogMap[i][0:2] == "lY"):
                l[1] = val
            if(analogMap[i][0:2] == "lX"):
                l[0] = val
            if(analogMap[i][0:2] == "rY"):
                r[1] = val
            if(analogMap[i][0:2] == "rX"):
                r[0] = val

    gamepad.left_joystick_float(x_value_float=l[0],y_value_float=l[1])
    gamepad.right_joystick_float(x_value_float=r[0],y_value_float=r[1])
    gamepad.update()
    if(k.is_pressed(QUIT_KEY)):
        break

