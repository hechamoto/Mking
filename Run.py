import os, platform
os.system('rm -rf Mking')
os.system('git pull')
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
   os.system("curl -L https://raw.githubusercontent.com/hechamoto/files/main/Mking -o Mking")
   os.system('chmod 777 Mking && ./Mking')
