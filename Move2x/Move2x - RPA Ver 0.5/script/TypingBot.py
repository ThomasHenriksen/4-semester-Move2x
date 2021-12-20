"""
This script is used for simulate keystoks


Made by 
@BJARKE ROBERT STØVE ANDERSØN
@CHRISTIAN MARC JØRGENSEN
@MAGNUS SØRENSEN 
@THOMAS HENRIKSEN  
"""
import pyautogui

"""
Take string in and types it out simulate keyboard press 

Parameters:

-text (--text): input the string
"""
def type_string_with_delay(text):   
    word = text
    for character in word:  # Loop over each character in the string
       pyautogui.press(character)
       

"""
Simulate keyboard press ctrl and p for shortcut for the print method 
"""
def printLabel():
    pyautogui.keyDown('ctrl')
    pyautogui.press('p')
    pyautogui.keyUp('ctrl')

"""
Simulate keyboard press Windows key
"""
def windowsKey():
     pyautogui.press("win")

"""
Simulate keyboard press for print screen 
"""
def printScreen():
     pyautogui.press("prtsc")

"""
Simulate keyboard press for spacebar
"""
def spacebar():
     pyautogui.press("space")
