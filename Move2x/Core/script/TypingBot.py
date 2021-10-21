import time
import random
from pynput.keyboard import Controller, Key
import sys
import os

keyboard = Controller()  # Create the controllerl

def type_string_with_delay(text):
    chooseword = text[1]
    for character in chooseword:  # Loop over each character in the string
        keyboard.type(character)  # Type the character
        delay = random.uniform(0, 2)  # Generate a random number between 0 and 10
        time.sleep(0.05)  # Sleep for the amount of seconds generated



