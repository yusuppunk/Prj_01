#-*- coding:utf-8 -*-
from socket import *

def scan(host,port):
    try:
        s = socket(AF_INET,SOCK_STREAM)
        s.settimeout(1)
        s.connect((host,port))
        print '[*] %d open' % port
    except:
        pass
def main():
    for p in range(1,600):
        scan('127.0.0.1',p)

if __name__=='__name__':
    main()