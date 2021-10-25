import time
import random
import pyautogui
import sys
import os



def type_string_with_delay(text):
    chooseword = text
    for character in chooseword:  # Loop over each character in the string
       pyautogui.press(character)
       time.sleep(0.05)  # Sleep for the amount of seconds generated

def print():
    pyautogui.keyDown('ctrl')
    pyautogui.press('p')
    pyautogui.keyUp('ctrl')