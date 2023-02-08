#/bin/python/
#librerias 
import os, time 
import subprocess
#Colores
RED = "\033[1;31m"
GREEN = "\033[0;32m"
BLUE = "\033[1;34m"
PURPLE = "\033[1;35m"
WHITE = "\033[1;37m"
#Descargas whatweb
#os.system('sudo apt-get install whatweb')
#os.system('clear')
#time.sleep(0.5)
#logo
banner = """
 ____   ____  ____  _   _  __        _______ ____  
/ ___| / ___|/ __ \| \ | | \ \      / /___ /| __ ) 
\___ \| |   / / _` |  \| |  \ \ /\ / /  |_ \|  _ \ 
 ___) | |__| | (_| | |\  |   \ V  V /  ___) | |_) | (By R3D-GHOST)
|____/ \____\ \__,_|_| \_|    \_/\_/  |____/|____/ 
             \____/                                

"""    
os.system("clear")
print(PURPLE+banner)
#menu opciones
print(GREEN+"1 --> Fast Scan Web")
print(BLUE+"2 --> Port Scan Web")
print(RED+"3 --> Exit")
opciones = input(WHITE+"Elige una Opcion >>> ")
if  opciones == "1":
    print("Coloca la url de pagina web Ejemplo https://www.google.com")
    print("Siempre con el https / http ")
    url = input('--->  ')
    whatweb = subprocess.getoutput('sudo whatweb --no-error -v ' + str(url))
    print(GREEN+whatweb)
elif opciones == "2":
    print("Esta Opcion Puede tardar un poco")
    time.sleep(2)
    os.system('clear')
    print("Coloca la IP o URL de la web")
    scan = input("--->  ")
    nmap = subprocess.getoutput('sudo nmap  nmap -Pn --open -v -A ' + str(scan))
    print(BLUE+nmap)
elif opciones == "3":
    exit
else:
    print("Invalid error")
