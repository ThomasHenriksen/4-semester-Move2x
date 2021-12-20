"""
This script is used for simulate mouse click


Made by 
@BJARKE ROBERT STØVE ANDERSØN
@CHRISTIAN MARC JØRGENSEN
@MAGNUS SØRENSEN 
@THOMAS HENRIKSEN  
"""
import pyautogui as pg 


"""
Simulate mouse press by coordinates 

Parameters:

-screenLocation (--screenLocation): input the coordinates where to press
"""
def Click_coord (screenLocation):
    pg.click(screenLocation)
