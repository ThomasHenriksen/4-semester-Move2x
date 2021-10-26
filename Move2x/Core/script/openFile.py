import subprocess

path_to_notepad = 'C:\Program Files (x86)\DYMO\DYMO Label Software\DLS.exe'
path_to_file = 'resources\\Label.label'

subprocess.call([path_to_notepad, path_to_file])