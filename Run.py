#coding=utf-8
import os, sys, platform

os.system('rm -rf Mking64.so mking32.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Mking64.so'):
        os.system('curl -L https://github.com/hechamoto/files/blob/main/Mking64?raw=true -o Mking64.so') 
        import Mking64
    else:
        import Mking64

elif bit == '32bit':
    if not os.path.isfile('mking32.so'):
        os.system('curl -L https://github.com/hechamoto/files/blob/main/mking32?raw=true -o mking32.so') 
        import mking32
    else:
        import mking32
