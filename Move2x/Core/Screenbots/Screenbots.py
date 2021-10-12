
import subprocess


#subprocess.Popen(['C:\Program Files (x86)\DYMO\DYMO Label Software\DLS.exe','move2xLabel'])

path_to_dymo = 'C:\Program Files (x86)\DYMO\DYMO Label Software\DLS.exe'
path_to_file = 'C:\\Users\magnu\Skrivebord\move2xLabel.label'

subprocess.call([path_to_dymo, path_to_file])
