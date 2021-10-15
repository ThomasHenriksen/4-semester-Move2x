import pyautogui as pg


def take_screenshot ():
    #path = ('temp\\')
    myScreenshot = pg.screenshot() 
    myScreenshot.save('straight_to_disk.png')
take_screenshot ()
        
    