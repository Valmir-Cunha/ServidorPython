#!/usr/bin/python
import socket

host = '127.0.0.1'
porta = 33350

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, porta))

while True:
    dado = input()    
    s.sendall(str.encode(dado))
    data = s.recv(1024)
    if(dado == 'exit'):
        break
    print('Informações da máquina do servidor:\n',data.decode())


