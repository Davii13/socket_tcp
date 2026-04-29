# 🚀 Socket TCP Concorrente em Python

Este projeto demonstra a implementação de uma arquitetura **Cliente-Servidor Multiponto** utilizando Sockets TCP e Threads em Python. O objetivo é validar a capacidade de um servidor TCP em gerenciar múltiplas conexões simultâneas de forma eficiente.

---

## 📂 Estrutura do Projeto

Abaixo está a organização dos arquivos no repositório:

```text
socket_tcp/
├── 📂 codigos/                 # Código-fonte original
│   ├── socket_tcp_concorrente_cliente.py
│   └── sockete_tcp_concorrente_servidor.py
├── 📂 imagens de teste/         # Evidências de funcionamento
│   ├── cliente 1.png
│   ├── cliente 2.png
│   ├── cliente 3.png
│   └── servidor.png
├── 📂 relatorio/                # Documentação formal
│   └── Relatorio.pdf
└── 📄 README.md                 # Documentação principal
```

---

## ✨ Funcionalidades

- **Servidor Multithread:** Utiliza a biblioteca `_thread` para processar conexões sem bloquear o loop principal.
- **Comunicação Direta:** Envio de strings via socket stream (TCP).
- **Escalabilidade Simples:** Configurado para aceitar uma fila de até 5 conexões pendentes (`listen(5)`).
- **Localhost:** Configurado para IP `127.0.0.1`, ideal para testes de rede em ambiente local.

---

## 🛠️ Pré-requisitos

- **Python 3.x** instalado.
- Bibliotecas nativas: `socket` e `_thread` (já inclusas no Python).

---

## 🚀 Como Rodar e Testar

Siga exatamente os passos abaixo para validar o funcionamento:

### 1. Iniciar o Servidor
Abra um terminal na pasta do projeto e execute:
```bash
python "codigos/sockete_tcp_concorrente_servidor.py"
```
O terminal exibirá: `Servidor TCP concorrente iniciado no IP 127.0.0.1 na porta 50000`.

### 2. Iniciar os Clientes
Abra **três ou mais terminais independentes** e em cada um deles execute:
```bash
python "codigos/socket_tcp_concorrente_cliente.py"
```
Você verá a mensagem: `Digite suas mensagens. Para sair, digite "sair" ou pressione Enter vazio.`

### 3. Validar a Concorrência
- Digite mensagens em terminais diferentes.
- Observe que o servidor recebe todas, identificando cada cliente por sua porta efêmera.
- No terminal do servidor, você verá mensagens como: `Nova thread iniciada para essa conexão` e `Cliente conectado: ('127.0.0.1', porta)`.

---

## 🧪 Resultados

Abaixo estão as capturas de tela que comprovam a execução simultânea das instâncias.

### 💻 Visão dos Clientes (Terminais Independentes)

| Cliente 1 | Cliente 2 | Cliente 3 |
| :---: | :---: | :---: |
| ![Mensagem Cliente 1](imagens%20de%20teste/cliente%201.png) | ![Mensagem Cliente 2](imagens%20de%20teste/cliente%202.png) | ![Mensagem Cliente 3](imagens%20de%20teste/cliente%203.png) |

### 🖥️ Visão Consolidada do Servidor

![Terminal do Servidor](imagens%20de%20teste/servidor.png)

---

## 📖 Explicação Técnica

O sistema baseia-se no modelo **Client-Server Multithread**:

1.  **Handshake TCP:** Ocorre no momento do `tcp.connect()`.
2.  **Threads:** O servidor utiliza `_thread.start_new_thread()` para que cada cliente tenha seu próprio fluxo de execução, permitindo que outros clientes se conectem ao mesmo tempo.
3.  **Portas Efêmeras:** Cada conexão de cliente utiliza uma porta distinta gerada pelo SO, o que permite ao servidor diferenciar as origens das mensagens.
4.  **Localhost (127.0.0.1):** Utilizado para garantir que os testes funcionem em qualquer máquina sem necessidade de configuração de rede física ou firewall.

---

## 👨‍💻 Autores

- **Davi Nunes Carvalho**
- **João Victor Russo Marquito**

*Trabalho prático desenvolvido para a disciplina de Redes de Computadores.*

