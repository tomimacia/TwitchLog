import pyautogui as pt
import time

def locateAndClick(img):
    src = pt.locateCenterOnScreen(img, confidence=0.8)
    time.sleep(0.3)
    pt.moveTo(src)
    time.sleep(0.3)
    pt.click()
    time.sleep(0.3)

def closeTab():
    pt.keyDown('ctrl')
    time.sleep(.2)
    pt.press('w')
    time.sleep(.2)
    pt.keyUp('ctrl')

def minimizar():
    time.sleep(5)
    pt.keyDown('win')
    time.sleep(.2)
    pt.press('m')
    time.sleep(.2)
    pt.keyUp('win')

