# Relatório Técnico: Comunicação Sockets TCP Concorrentes

**Disciplina:** Redes de Computadores  
**Professor:** Marco Aurélio de Souza Birchal  

---

## 1. Enunciado da Atividade
Implementar e testar os códigos de comunicação multiponto utilizando Sockets TCP e Threads em Python, baseados no material `REDES3_ES_TCP_Sockets_Parte2.pdf`. 

O objetivo é validar a capacidade de um servidor TCP em gerenciar múltiplas conexões simultâneas (concorrência) através de threads.

> **Nota de Configuração:** Conforme solicitado, o endereço IP nos códigos foi ajustado para `127.0.0.1` (localhost) para permitir a execução e teste local sem dependência de redes externas.

---

## 2. Códigos Implementados

### 2.1. Servidor Concorrente (`sockete_tcp_concorrente_servidor.py`)
O servidor foi projetado para escutar na porta `50000` e, para cada nova conexão aceita, disparar uma thread independente para processar as mensagens do cliente sem bloquear o loop principal.

```python
# -*- coding: utf-8 -*-
import socket
import _thread

HOST = '127.0.0.1' # Endereco IP do Servidor
PORT = 50000       # Porta que o Servidor está

# Função chamada quando uma nova thread for iniciada
def conectado(con, cliente):
    print('\nCliente conectado:', cliente)
    while True:
        msg = con.recv(1024)
        if not msg:
            break
        print('\nCliente..:', cliente)
        print('Mensagem.:', msg.decode())

    print('\nFinalizando conexao do cliente', cliente)
    con.close()
    _thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(5) # Permite até 5 conexões na fila de espera

print('\nServidor TCP concorrente iniciado no IP', HOST, 'na porta', PORT)

try:
    while True:
        con, cliente = tcp.accept()
        print('\nNova thread iniciada para essa conexão')
        _thread.start_new_thread(conectado, tuple([con, cliente]))
except KeyboardInterrupt:
    print('\nFinalizando o servidor...')
finally:
    tcp.close()
```

### 2.2. Cliente TCP (`socket_tcp_concorrente_cliente.py`)
O cliente estabelece uma conexão via stream (TCP) com o servidor e permite o envio de mensagens em loop até que o usuário decida encerrar.

```python
import socket

HOST = '127.0.0.1' # Endereco IP do Servidor
PORT = 50000       # Porta que o Servidor está

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)

try:
    tcp.connect(destino)
    print('\nDigite suas mensagens. Para sair, digite "sair" ou pressione Enter vazio.')
    
    while True:
        mensagem = input('Sua mensagem: ')
        
        if mensagem.lower() == 'sair' or not mensagem:
            break
            
        tcp.send(mensagem.encode())
        
except Exception as e:
    print(f'\nErro: {e}')
finally:
    print('\nFechando conexão...')
    tcp.close()
```

---

## 3. Resultados da Execução

Abaixo estão as capturas de tela que comprovam a execução simultânea de três instâncias do cliente enviando mensagens para o servidor central.

### 💻 Clientes em Execução (Terminais Independentes)

| Cliente 1 | Cliente 2 | Cliente 3 |
| :---: | :---: | :---: |
| ![Mensagem Cliente 1](imagens%20de%20teste/cliente%201.png) | ![Mensagem Cliente 2](imagens%20de%20teste/cliente%202.png) | ![Mensagem Cliente 3](imagens%20de%20teste/cliente%203.png) |
| *Instância 1* | *Instância 2* | *Instância 3* |

### 🖥️ Visão Consolidada do Servidor
O servidor identifica cada conexão por meio do par `(IP, Porta Efêmera)`. Note que cada cliente possui uma porta de origem única (ex: 51234, 51235, etc.), permitindo que o servidor direcione as respostas corretamente através das threads.

![Terminal do Servidor](imagens%20de%20teste/servidor.png)
*Legenda: Servidor processando múltiplas threads simultaneamente.*

---

## 4. Explicação Técnica do Funcionamento

O sistema baseia-se no modelo **Client-Server Multithread**:

1.  **Handshake TCP:** Quando o cliente executa `tcp.connect()`, ocorre o "Three-way Handshake" para estabelecer uma conexão confiável.
2.  **Concorrência via Threads:** O servidor utiliza a função `_thread.start_new_thread()`. Isso permite que o processo pai continue executando o `tcp.accept()` para ouvir novos clientes, enquanto o processo filho (thread) cuida exclusivamente da comunicação com o cliente já conectado.
3.  **Portas Efêmeras:** Embora o servidor utilize a porta fixa `50000`, o sistema operacional atribui portas aleatórias (efêmeras) para cada cliente, o que possibilita a distinção entre as conexões.
4.  **Localhost (127.0.0.1):** O uso deste IP garante que a comunicação ocorra dentro da pilha de rede interna do computador, ideal para testes de desenvolvimento e isolamento de problemas de rede física.

---
*Relatório desenvolvido como parte das atividades práticas da disciplina de Redes de Computadores.*
