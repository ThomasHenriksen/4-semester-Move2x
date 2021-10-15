import pyautogui as pg 
from SearchBot import max_loc

def Click_coord ():
    x, y = max_loc
    max_loc = x + 20, y + 20
    pg.click(max_loc)
Click_coord()
