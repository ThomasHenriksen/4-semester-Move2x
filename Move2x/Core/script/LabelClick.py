import pyautogui as pg 


def Click_coord (max_loc):
    x, y = max_loc
    max_loc = x + 20, y + 20
    pg.click(max_loc)
