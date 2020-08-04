import webbrowser as wb
import pyautogui as pag
from fetch import url
import time
import cv2

print(pag.size())
wb.open_new_tab(url)
print("start locating")
time.sleep(10)
loc = pag.locateCenterOnScreen('join.png',confidence = 0.8)
pag.moveTo(loc)
time.sleep(2)
pag.click(loc)
print(loc)