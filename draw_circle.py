import pyautogui
import math 
import time 
STEP = 6
# Radius 

# print(pyautogui.position())
R = 100
# measuring screen size
time.sleep(5)
(x,y) = pyautogui.size()
# locating center of the screen 
(X,Y) = pyautogui.position()
# offsetting by radius 
time.sleep(1)
pyautogui.moveTo(X+R,Y)
pyautogui.mouseDown()
for angle_deg in range(0, 370,STEP):
    angle_rad = math.radians(angle_deg)
    pyautogui.moveTo(
            X + R * math.cos(angle_rad),
            Y + R * math.sin(angle_rad))
pyautogui.mouseUp()