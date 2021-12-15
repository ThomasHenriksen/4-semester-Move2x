import time
import random
import pyautogui
import sys
import os



def type_string_with_delay(text):   
    word = text
    for character in word:  # Loop over each character in the string
       pyautogui.press(character)
       

def printLabel():
    pyautogui.keyDown('ctrl')
    pyautogui.press('p')
    pyautogui.keyUp('ctrl')

def windowsKey():
     pyautogui.press("win")
def printScreen():
     pyautogui.press("prtsc")
def spacebar():
     pyautogui.press("space")
