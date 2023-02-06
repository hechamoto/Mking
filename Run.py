#coding=utf-8
import os, sys, platform

os.system('rm -rf Mking64.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('Mking64.so'):
        os.system('curl -L https://raw.githubusercontent.com/hechamoto/files/main/Mking64.so -o Mking64.so') 
        import Mking64
    else:
        import Mking64
