import time
import random
from pynput.keyboard import Controller, Key
import sys
import os

keyboard = Controller()  # Create the controllerl

os.startfile('C:\\Users\\Bjark\\Desktop\\Testdokument.docx')


def type_string_with_delay(string):
    for character in string:  # Loop over each character in the string
        keyboard.type(character)  # Type the character
        delay = random.uniform(0, 2)  # Generate a random number between 0 and 10
        time.sleep(0.25)  # Sleep for the amount of seconds generated

type_string_with_delay("This is my string typed with a delay")

sys.exit

