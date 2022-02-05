#!/usr/bin/python
import socket
import sys
for porta in range(1,65535):
         meusocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Aqui definimos ja nosso socket em tcp
         if meusocket.connect_ex((sys.argv[1],porta)) == 0:
         	banner = meusocket.recv(1024)
         	print ("Porta",porta,"[ABERTA]","[SERVIÇO]",banner)
         	meusocket.close()

