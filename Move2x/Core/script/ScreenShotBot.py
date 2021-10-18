import pyautogui as pg


def take_screenshot ():
    temp = 'temp\\'
    type = '.png'
    name = 'ScreenShot'
    path = temp + name + type     
    myScreenshot = pg.screenshot() 
    myScreenshot.save(path)
    return name
        
    