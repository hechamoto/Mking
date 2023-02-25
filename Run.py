import os, platform
os.system('rm -rf Mking64.so')
os.system('git pull')
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Mking64.so'):
    os.system("curl -L https://raw.githubusercontent.com/hechamoto/files/main/Mking64.so -o Mking64.so")
        import Mking64
    else:
        import Mking64
