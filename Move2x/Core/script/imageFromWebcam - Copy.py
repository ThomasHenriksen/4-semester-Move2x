import glob
import os
from PIL import Image
from pathlib import Path

def takeImageFromWebcamFolder():
    list_of_files = glob.glob('D:\*') 
    latest_file = max(list_of_files, key=os.path.getctime)


    my_filePNG = Path("Temp\\webcam.png")
    if my_filePNG.is_file():
        os.remove("Temp\\webcam.png")

    os.rename(latest_file, "Temp\\webcam.jpg")
    im = Image.open('Temp\\webcam.jpg')
    im.save('Temp\\webcam.png')

    my_fileJPG = Path("Temp\\webcam.jpg")
    if my_fileJPG.is_file():
        os.remove("Temp\\webcam.jpg")

    list_of_files = glob.glob('Temp\\*') 
    latest_file = max(list_of_files, key=os.path.getctime)
   
takeImageFromWebcamFolder()
