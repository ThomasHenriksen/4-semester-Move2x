import time
import random
from pyautogui import press
import sys
import os



def type_string_with_delay(text):
    chooseword = text[1]
    for character in chooseword:  # Loop over each character in the string
        press(character)
        time.sleep(0.05)  # Sleep for the amount of seconds generated

