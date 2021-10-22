import pyautogui as pg


def take_screenshot (window):
    temp = 'temp\\'
    type = '.png'
    name = window
    path = temp + name + type     
    myScreenshot = pg.screenshot() 
    myScreenshot.save(path)
    return name
        
    