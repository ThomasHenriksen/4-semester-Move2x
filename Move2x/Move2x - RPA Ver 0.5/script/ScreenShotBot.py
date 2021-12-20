"""
This script is used for screen shot of the current window 


Made by 
@BJARKE ROBERT STØVE ANDERSØN
@CHRISTIAN MARC JØRGENSEN
@MAGNUS SØRENSEN 
@THOMAS HENRIKSEN  
"""



from PIL import ImageGrab
import os
from pathlib import Path
import time
from script import TypingBot as typingBot
"""
This method is used for take a screen shot

Parameters:

-window (--string): input a name for a image

Return: 

-name (--string): output the name of the image
"""
def take_screenshot (window):
   
    time.sleep(0.2)
    name = window
    temp = 'temp\\'
    type = '.png'
    path = temp + name + type
    typingBot.printScreen()
    try:
        im = ImageGrab.grabclipboard()
    except:
        take_screenshot (window)
    my_filePNG = Path(path)
    if my_filePNG.is_file():
         os.remove(my_filePNG)
    im.save(path)

    return name

