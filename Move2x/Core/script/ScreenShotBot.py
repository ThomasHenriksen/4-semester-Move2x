import pyautogui as pg
from PIL import ImageGrab
import os
from pathlib import Path
import time
from script import TypingBot as typingBot

def take_screenshot (window):
    time.sleep(0.1)
    name = window
    temp = 'temp\\'
    type = '.png'
    path = temp + name + type
    typingBot.printScreen()
    im = ImageGrab.grabclipboard()
    my_filePNG = Path(path)
    if my_filePNG.is_file():
         os.remove(my_filePNG)
    im.save(path)



   # path = temp + name + type     
   # myScreenshot = pg.screenshot() 
   # myScreenshot.save(path)
    return name

