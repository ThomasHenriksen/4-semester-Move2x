"""
This script is used for opening DYMO Label Software, deleting the old template and make a new template by copy it from the backup 


Made by 
@BJARKE ROBERT STØVE ANDERSØN
@CHRISTIAN MARC JØRGENSEN
@MAGNUS SØRENSEN 
@THOMAS HENRIKSEN  
"""
import subprocess
import shutil
import os
from pathlib import Path


"""
This method is used to open DYMO Label Software and open the template for the label
"""
def openFile():
    path_to_notepad = 'C:\Program Files (x86)\DYMO\DYMO Label Software\DLS.exe'
    path_to_file = 'resources\\Label.label'
    subprocess.Popen([path_to_notepad, path_to_file])
    
"""
This method is used to delete the old file 
"""
def deleteFile():
    my_filePNG = Path("resources\\Label.label")
    if my_filePNG.is_file():
        os.remove("resources\\Label.label")

"""
This method is used to make a copy of the Backup template and makes the copy to the new template 
"""
def copyFile():
    # Source path
    source = "resources\\newBackUp.label"
 
    # Destination path
    destination = "resources\\Label.label"
 
    # Copy the content of
    # source to destination
    shutil.copyfile(source, destination)
  

