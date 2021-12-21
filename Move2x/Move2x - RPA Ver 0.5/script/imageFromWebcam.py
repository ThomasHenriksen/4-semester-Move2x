"""
This script is used for takning the image from Logitech Capture default folder 


Made by 
@BJARKE ROBERT STØVE ANDERSØN
@CHRISTIAN MARC JØRGENSEN
@MAGNUS SØRENSEN 
@THOMAS HENRIKSEN  
"""

import glob
import os
from PIL import Image
from pathlib import Path
import shutil

"""
This method is used for getting the name of the newest file in the Logitech Capture default folder 

Return:

-latest_file (--latest_file): outputs the name of the last file in the folder 

"""
def pathToFile():
    list_of_files = glob.glob(webcamFolder()) 
    latest_file = max(list_of_files, key=os.path.getctime)
    print(latest_file )
    return latest_file

"""
This method is used for getting the newest file in the Logitech Capture default folder, 
its removes the old image and then moves the new file in to the temp folder 
"""
def takeImageFromWebcamFolder():
    folder = '/temp/*'
    files = glob.glob(folder)
    for file in files:
        os.remove(file)
    path = pathToFile()
    
    src_dir = os.getcwd()
    dest_file = src_dir + "/temp/webcam.jpg"

    my_filePNG = Path("Temp\\webcam.png")
    if my_filePNG.is_file():
        os.remove("Temp\\webcam.png")

    shutil.move(path, dest_file)

    im = Image.open('Temp\\webcam.jpg')
    im.save('Temp\\align.png')
    os.remove("Temp\\webcam.jpg")    

"""
This method is used for path to the Logitech Capture default folder 

Return:

-text (--string): outputs the path to Logitech Capture default folder 
"""   
def webcamFolder():
    return 'C:\\Users\\festo\\Videos\\Logitech\\LogiCapture\\*.jpg'

