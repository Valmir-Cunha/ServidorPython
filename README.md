# Servidor: Requisição de sistema

## Valmir Vinicius da Cunha Rezende

 
Devido a falta de conhecimento prévio do aluno com a linguagem python, o servidor trata-se de um código simples, onde recebe uma requisição do cliente e retorna informações sobre a máquina em que está rodando.

O repositório esta dividido em duas parte:

Atividade Servidor: Referente a criação do servidor em python, sem uso de docker.

Atividade Docker: Referente a criação do docker onde ficará o servidor.

##  Porta do servidor:

>33350

## Exemplo de uso:

Atividade do servidor:

Guia para utilizar: Instale o sudo pip install psutil, após isso execute o arquivo servidor.py e logo em seguida o cliente.py, em seguida digite o comando desejado no terminal de execução do cliente.py .

Envio do comando "info" pelo usuário, o retorno será:
Informações da máquina do servidor:
A porcentagem de uso da CPU é: xx.x
A porcentagem de uso da memoria RAM é: xx.x
Sistema operacional do servidor: Nome do sistema
Quantidade de nucleos: x


Exemplo na máquina do aluno do comando 'info':
Informações da máquina do servidor:
A porcentagem de uso da CPU é:12.3
A porcentagem de uso da memoria RAM é: 44.3
Sistema operacional do servidor:Windows
Quantidade de nucleos: 4


------------------------------------------------------------------------------------------------

Atividade docker:

Atrvés do terminal, acesse o diretorio: cd Atividade_docker/

Dentro do diretório, para construir a imagem e criar o contâiner, execute o comando: docker-compose up --build

Após isso, o servidor já estará em execução, para realizar um teste é necessário a execução do arquivo cliente.py. Após a execução digite o comando desejado para teste.



