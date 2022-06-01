#!/usr/bin/python

#Necessario executar o seguinte comando: sudo pip install psutil

#Servidor que recebe um comando e retorna informações do sistema

import socket
import platform
import psutil 
import os 


host = 'localhost'
porta = 33350

#Trabalhando com IPv4 e TCP
servico = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Definindo os servidores e portas
servico.bind((host,porta))
#Colocando o servidor em modo de escuta
servico.listen()
conexao, endereco = servico.accept()
#troca de mensagens
while True:
    dado = conexao.recv(1024)
    if (dado.decode() == 'exit'):
        print('Fim da conexão') 
        conexao.close()
        break
    if(dado.decode() == 'usage'):
        conexao.sendall(str.encode('A porcentagem de uso da CPU é: ' + str(psutil.cpu_percent(2)) + '\n'
            'A porcentagem de uso da memoria RAM é: ' + str(psutil.virtual_memory()[2])))
    elif(dado.decode() == 'system'):
        conexao.sendall(str.encode('Sistema operacional do servidor:' + platform.system()))
    elif(dado.decode() == 'kernel'):
        conexao.sendall(str.encode('Quantidade de nucleos: ' + str(os.cpu_count())))
    elif(dado.decode() == 'info'):
        conexao.sendall(str.encode('A porcentagem de uso da CPU é: ' + str(psutil.cpu_percent(2)) + '\n'
            'A porcentagem de uso da memoria RAM é: ' + str(psutil.virtual_memory()[2])+ '\n'
            'Sistema operacional do servidor:' + platform.system() + '\n'
            'Quantidade de nucleos: ' + str(os.cpu_count())))
    else:
        conexao.sendall(str.encode('Comando inválido\n'
        'Lista de comandos:\n'
        'usage - Para informação de uso da CPU e RAM\n'
        'system - Para informar o sistema operacional usado no servidor\n'
        'kernel - Para informar a quantidade de núcleos no cpu\n'
        'info - Para todas as informações disponíveis'))
servico.close()