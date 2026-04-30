# 🌐 Redes de Computadores: Implementação de Sockets (TCP, UDP e TCP Concorrente)

Este repositório contém os projetos e relatórios das atividades práticas da disciplina de Redes de Computadores. 
O objetivo das implementações é explorar os modelos de comunicação **Cliente-Servidor** utilizando diferentes abordagens e protocolos na camada de transporte:
- **UDP (User Datagram Protocol)**: Comunicação rápida sem conexão.
- **TCP (Transmission Control Protocol) Simples**: Comunicação confiável e orientada a conexão.
- **TCP Concorrente com Threads**: Comunicação confiável permitindo o gerenciamento simultâneo de múltiplos clientes conectados ao mesmo servidor.

---

## 📁 Estrutura do Repositório

```text
socket_tcp/
│
├── codigos/
│   ├── TCPClient.py                            # Cliente TCP Simples
│   ├── TCPServer.py                            # Servidor TCP Simples
│   ├── UDPClient.py                            # Cliente UDP Simples
│   ├── UDPServer.py                            # Servidor UDP Simples
│   ├── socket_tcp_concorrente_cliente.py       # Cliente para comunicação multithread TCP
│   └── sockete_tcp_concorrente_servidor.py     # Servidor multithread (concorrente) TCP
│
├── relatório/
│   ├── Relatorio.pdf                           # Relatório técnico completo (PDF original)
│   └── relatorio.md                            # Versão em Markdown do relatório técnico
│
├── imagens de teste/                           # Capturas de tela das execuções (concorrência)
└── README.md                                   # Documentação atual
```

---

## 🚀 Como Executar os Códigos

Todos os códigos estão configurados para operar no IP local (`127.0.0.1` ou `localhost`), utilizando a porta `12000` para os testes simples (TCP/UDP) e a porta `50000` para o teste concorrente.

### 1. Comunicação UDP Simples
Este exemplo envia uma frase em letras minúsculas para o servidor via datagramas UDP. O servidor transforma o texto em letras maiúsculas e devolve ao cliente.

1. Abra um terminal e inicie o Servidor UDP:
   ```bash
   python codigos/UDPServer.py
   ```
2. Abra outro terminal e inicie o Cliente UDP:
   ```bash
   python codigos/UDPClient.py
   ```
3. Digite a mensagem no cliente e observe o retorno.

### 2. Comunicação TCP Simples
Similar ao UDP, porém garante a entrega dos pacotes por meio do estabelecimento de uma conexão ("three-way handshake").

1. Abra um terminal e inicie o Servidor TCP:
   ```bash
   python codigos/TCPServer.py
   ```
2. Abra outro terminal e inicie o Cliente TCP:
   ```bash
   python codigos/TCPClient.py
   ```
3. Digite a mensagem no cliente e observe o retorno em maiúsculas.

### 3. Comunicação TCP Concorrente (Multithread)
Este servidor permite que vários clientes se conectem **simultaneamente**, criando uma Thread (tarefa em segundo plano) individual para cada conexão recebida.

1. **Iniciando o Servidor Concorrente**:
   Abra um terminal, acesse a pasta do repositório e execute:
   ```bash
   python codigos/sockete_tcp_concorrente_servidor.py
   ```
   *O servidor ficará em modo de espera aguardando conexões simultâneas.*

2. **Iniciando os Clientes**:
   Abra **vários terminais** (quantos desejar testar) e execute em cada um deles:
   ```bash
   python codigos/socket_tcp_concorrente_cliente.py
   ```
3. **Teste Prático**:
   - Envie mensagens de diferentes terminais para o servidor e observe o log sendo impresso de forma independente, sem causar travamentos nas outras conexões.
   - Digite `sair` para encerrar a conexão de um cliente específico.

---

## 📄 Relatório Completo

Para uma explicação técnica profunda, detalhando o comportamento das threads, o "Three-way handshake" do TCP, portas efêmeras e análises do uso das bibliotecas do Python, consulte o **[Relatório em Markdown](relatório/relatorio.md)** ou a versão original em PDF localizada na pasta `relatório/`.
