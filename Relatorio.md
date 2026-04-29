# RELATÓRIO DE ATIVIDADE PRÁTICA: SOCKETS TCP CONCORRENTES

**Instituição:** Curso de Engenharia/TI  
**Disciplina:** Redes de Computadores  
**Professor:** Marco Aurélio de Souza Birchal  
**Assunto:** Implementação de Servidor TCP Multithread em Python  

---

## 1. INTRODUÇÃO
Este relatório documenta a implementação de um sistema de comunicação cliente-servidor utilizando o protocolo TCP (Transmission Control Protocol). O foco principal é a demonstração de um **Servidor Concorrente**, capaz de atender múltiplos clientes simultaneamente através do uso de threads.

## 2. REQUISITOS DA ATIVIDADE
Conforme o enunciado proposto:
- Implementar os códigos do slide `REDES3_ES_TCP_Sockets_Parte2.pdf`.
- Apresentar o código-fonte completo.
- Demonstrar a execução com capturas de tela.
- Explicar o funcionamento técnico dos programas.
- Adaptar o host para `127.0.0.1` ou `localhost`.

## 3. ARQUITETURA DO SISTEMA

### 3.1. Servidor (`sockete_tcp_concorrente_servidor.py`)
O servidor opera em modo passivo. Suas principais etapas são:
1. **Criação do Socket:** Utiliza `AF_INET` (IPv4) e `SOCK_STREAM` (TCP).
2. **Bind:** Vincula o socket ao IP `127.0.0.1` e porta `50000`.
3. **Listen:** Entra em estado de escuta.
4. **Accept & Threading:** Ao receber uma conexão, o servidor não para seu loop; ele cria uma nova thread (`_thread.start_new_thread`) para lidar com aquele cliente específico e volta imediatamente a esperar por novas conexões.

### 3.2. Cliente (`socket_tcp_concorrente_cliente.py`)
O cliente opera em modo ativo:
1. **Connect:** Solicita conexão ao servidor.
2. **Loop de Mensagens:** Envia dados via `tcp.send()`.
3. **Encerramento:** Finaliza a conexão de forma limpa.

## 4. CÓDIGO FONTE

### 4.1. Servidor
```python
import socket
import _thread

HOST = '127.0.0.1'
PORT = 50000

def conectado(con, cliente):
    print('\nCliente conectado:', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print('\nCliente..:', cliente)
        print('Mensagem.:', msg.decode())
    con.close()
    _thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen(5)

print('\nServidor iniciado no IP', HOST, 'na porta', PORT)

while True:
    con, cliente = tcp.accept()
    _thread.start_new_thread(conectado, tuple([con, cliente]))
```

### 4.2. Cliente
```python
import socket

HOST = '127.0.0.1'
PORT = 50000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    tcp.connect((HOST, PORT))
    while True:
        mensagem = input('Sua mensagem: ')
        if mensagem.lower() == 'sair' or not mensagem: break
        tcp.send(mensagem.encode())
finally:
    tcp.close()
```

## 5. EVIDÊNCIAS DE EXECUÇÃO E TESTES

Para validar a concorrência, foram abertos 3 terminais de clientes simultâneos.

### 5.1. Conexões Simultâneas
As imagens abaixo mostram três clientes distintos operando ao mesmo tempo:

![Cliente 1](imagens%20de%20teste/cliente%201.png)
![Cliente 2](imagens%20de%20teste/cliente%202.png)
![Cliente 3](imagens%20de%20teste/cliente%203.png)

### 5.2. Log do Servidor
O servidor registrou o recebimento de todas as mensagens, comprovando que as threads funcionaram de forma independente para cada porta efêmera gerada pelo sistema operacional.

![Servidor Log](imagens%20de%20teste/servidor.png)

## 6. ANÁLISE TÉCNICA
A implementação demonstra o conceito de **Servidor de Alta Disponibilidade**. Em um servidor iterativo, o Cliente 2 teria que esperar o Cliente 1 desconectar para ser atendido. Com o uso de `Threads`, o tempo de resposta é imediato para todos os participantes, limitado apenas pelos recursos de hardware (CPU/RAM) e largura de banda.

## 7. CONCLUSÃO
A atividade foi concluída com sucesso. Os códigos foram adaptados para o ambiente local (`127.0.0.1`) e a comunicação TCP foi estabelecida de forma robusta e paralela, atendendo a todos os requisitos solicitados pelo Professor Marco Aurélio de Souza Birchal.
