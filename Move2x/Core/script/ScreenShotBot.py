import pyautogui as pg


def take_screenshot ():
    #path = ('temp\\')
    myScreenshot = pg.screenshot() 
    myScreenshot.save('ScreenShot.png')
    return myScreenshot
        
    