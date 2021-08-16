import pyautogui
import sys
import time
from datetime import datetime
pyautogui.FAILSAFE = False
print("Vasthav made Movement at {}".format(datetime.now()))
pyautogui.moveTo(100,200, duration=3600)
