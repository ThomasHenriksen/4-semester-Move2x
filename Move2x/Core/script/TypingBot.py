import time
import random
import pyautogui
import sys
import os



def type_string_with_delay(text):   
    word = text[0]
    for character in word:  # Loop over each character in the string
       print(character)
       pyautogui.press(character)
       time.sleep(0.05)  # Sleep for the amount of seconds generated

def printLabel():
    pyautogui.keyDown('ctrl')
    pyautogui.press('p')
    pyautogui.keyUp('ctrl')