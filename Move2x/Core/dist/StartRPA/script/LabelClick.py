import pyautogui as pg 


def Click_coord (screenLocation):
      
    x, y = screenLocation
    screenLocation = x + 20, y + 20
    pg.click(screenLocation)
