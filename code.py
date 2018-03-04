import pyautogui
import time

time.sleep(10)

file = open("dictionary.py","r")
for line in file:
	# for char in line:
	pyautogui.typewrite(line,0.0001)

file.close()