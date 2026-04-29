# -*- coding: utf-8 -*-
'''
Exemplo de um Servidor TCP Concorrente (Multithread)
Artigo: https://www.linkedin.com/pulse/python-sockets-criando-um-servidor-tcp-concorrente-
diego/
Diego Mendes Rodrigues
'''
import socket
import _thread

HOST = '127.0.0.1' # Endereco IP do Servidor
PORT = 50000 # Porta que o Servidor está

# Função chamada quando uma nova thread for iniciada
def conectado(con, cliente):
    print('\nCliente conectado:', cliente)
    while True:
        # Recebendo as mensagens através da conexão
        msg = con.recv(1024)
        if not msg:
            break
        print('\nCliente..:', cliente)
        print('Mensagem.:', msg.decode()) # Decode to string for better display

    print('\nFinalizando conexao do cliente', cliente)
    con.close()
    _thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

# Colocando um endereço IP e uma porta no Socket
tcp.bind(orig)

# Colocando o Socket em modo passivo
tcp.listen(5) # Aumentado para 5 para permitir mais conexões pendentes

print('\nServidor TCP concorrente iniciado no IP', HOST, 'na porta', PORT)

try:
    while True:
        # Aceitando uma nova conexão
        con, cliente = tcp.accept()
        print('\nNova thread iniciada para essa conexão')
        # Abrindo uma thread para a conexão
        _thread.start_new_thread(conectado, tuple([con, cliente]))
except KeyboardInterrupt:
    print('\nFinalizando o servidor...')
finally:
    # Fechando o Socket principal
    tcp.close()