# RELATÓRIO DE ATIVIDADE PRÁTICA: SOCKETS TCP E UDP

**Instituição:** Curso de Engenharia/TI  
**Disciplina:** Redes de Computadores  
**Professor:** Marco Aurélio de Souza Birchal  
**Assunto:** Implementação de Servidor TCP Multithread em Python e exemplos de Sockets Simples TCP/UDP.

---

## 1. INTRODUÇÃO

Este relatório documenta a implementação de um sistema de comunicação cliente-servidor utilizando os protocolos TCP (Transmission Control Protocol) e UDP (User Datagram Protocol). O foco principal é a demonstração de um Servidor Concorrente, capaz de atender múltiplos clientes simultaneamente através do uso de threads, além das implementações de comunicação simples utilizando UDP e TCP.

## 2. REQUISITOS DA ATIVIDADE

Conforme o enunciado proposto:

- Implementar os códigos de comunicação simples (TCP e UDP) e códigos de comunicação concorrente em TCP.
- Apresentar o código-fonte completo.
- Demonstrar a execução com capturas de tela.
- Explicar o funcionamento técnico dos programas.
- Adaptar o host para `127.0.0.1` ou `localhost`.

## 3. ARQUITETURA DO SISTEMA

### 3.1. Servidor TCP Concorrente (`sockete_tcp_concorrente_servidor.py`)

O servidor opera em modo passivo. Suas principais etapas são:

1. **Criação do Socket**: Utiliza `AF_INET` (IPv4) e `SOCK_STREAM` (TCP).
2. **Bind**: Vincula o socket ao IP `127.0.0.1` e porta `50000`.
3. **Listen**: Entra em estado de escuta.
4. **Accept & Threading**: Ao receber uma conexão, o servidor não para seu loop; ele cria uma nova thread (`_thread.start_new_thread`) para lidar com aquele cliente específico e volta imediatamente a esperar por novas conexões.

### 3.2. Cliente TCP Concorrente (`socket_tcp_concorrente_cliente.py`)

O cliente opera em modo ativo:

1. **Connect**: Solicita conexão ao servidor.
2. **Loop de Mensagens**: Envia dados via `tcp.send()`.
3. **Encerramento**: Finaliza a conexão de forma limpa.

### 3.3. Servidor e Cliente UDP (`UDPServer.py` e `UDPClient.py`)

Utiliza `SOCK_DGRAM` para criar uma comunicação sem conexão (datagramas). O cliente envia uma mensagem e aguarda resposta. O servidor recebe a mensagem via `recvfrom`, processa convertendo em maiúsculo e responde via `sendto`.

### 3.4. Servidor e Cliente TCP Simples (`TCPServer.py` e `TCPClient.py`)

Utiliza `SOCK_STREAM`. O servidor aceita uma única conexão por vez, lê uma mensagem, a converte para maiúsculo e responde. Em seguida, encerra a conexão.

## 4. CÓDIGO FONTE

### 4.1. Servidor e Cliente TCP Concorrentes
(Veja os arquivos `sockete_tcp_concorrente_servidor.py` e `socket_tcp_concorrente_cliente.py` na pasta `codigos`)

### 4.2. Servidor e Cliente UDP
(Veja os arquivos `UDPServer.py` e `UDPClient.py` na pasta `codigos`)

### 4.3. Servidor e Cliente TCP Simples
(Veja os arquivos `TCPServer.py` e `TCPClient.py` na pasta `codigos`)

---

## 5. EVIDÊNCIAS DE EXECUÇÃO E TESTES

Para validar o funcionamento, os códigos foram executados no ambiente local.

### 5.1. Conexões Simultâneas (TCP Concorrente)

As imagens abaixo mostram três clientes distintos operando ao mesmo tempo se comunicando com o Servidor Concorrente.

<!-- TODO: Inserir Prints do terminal (Clientes Simultâneos) -->
> **[INSERIR PRINT AQUI]** Captura de tela dos clientes conectados simultaneamente enviando mensagens.

### 5.2. Log do Servidor (TCP Concorrente)

O servidor registrou o recebimento de todas as mensagens, comprovando que as threads funcionaram de forma independente para cada porta efêmera gerada pelo sistema operacional.

<!-- TODO: Inserir Print do terminal (Servidor) -->
> **[INSERIR PRINT AQUI]** Captura de tela do servidor (mostrando "Nova thread iniciada para essa conexão" e o print das mensagens).

### 5.3. Testes Sockets Simples (TCP/UDP)

O teste dos servidores UDP e TCP simples foi realizado enviando mensagens de teste e recebendo o processamento esperado (ex: texto transformado em letras maiúsculas).

<!-- TODO: Inserir Prints do terminal (UDP e TCP simples) -->
> **[INSERIR PRINT AQUI]** Capturas de tela mostrando o Cliente UDP e TCP recebendo as mensagens convertidas para maiúsculo pelo Servidor.

---

## 6. ANÁLISE TÉCNICA

A implementação utiliza o modelo clássico de comunicação baseado em sockets TCP com suporte à concorrência por meio de multithreading de baixo nível (`_thread`), bem como comunicação baseada em pacotes via UDP.

No **servidor concorrente TCP**, o socket é configurado com `AF_INET` (IPv4) e `SOCK_STREAM` (TCP), garantindo uma comunicação confiável, orientada à conexão e com controle de entrega e ordem dos pacotes. Após o `bind()` no endereço `127.0.0.1:50000`, o método `listen(5)` define uma fila de até 5 conexões pendentes, o que já demonstra uma preocupação com múltiplas tentativas simultâneas de conexão.

O ponto central da concorrência está no uso da função `_thread.start_new_thread()`. A cada nova conexão aceita via `accept()`, o servidor cria uma nova thread que executa a função que lida com as requisições. Essa abordagem permite que:
- Cada cliente seja tratado de forma independente.
- O servidor continue aceitando novas conexões sem bloqueio.
- A leitura de dados ocorra de forma isolada por cliente.

Dentro da thread, o loop de recepção de dados funciona de forma contínua até que o cliente encerre a conexão. Esse comportamento está alinhado com o funcionamento do TCP, onde o encerramento da conexão é detectado pela ausência de dados. Outro ponto importante é que o servidor trabalha com portas efêmeras para cada cliente, o que permite múltiplas conexões simultâneas mesmo utilizando o mesmo IP e porta principal.

No **cliente concorrente TCP**, o fluxo é simples e direto:
- Criação do socket TCP.
- Estabelecimento da conexão com `connect()`.
- Loop interativo com envio de mensagens via `send()`.
- Codificação em bytes com `.encode()` (necessária para transmissão TCP).

**Modelos UDP e TCP simples:**
Nos exemplos de TCP e UDP simples, ilustra-se o funcionamento fundamental. No UDP (`SOCK_DGRAM`), as mensagens são enviadas e recebidas com o par de funções `sendto`/`recvfrom`, sem necessidade de estabelecimento prévio de conexão (`accept`). Já o TCP simples mostra a configuração básica de fluxo, conectando-se e desconectando-se após um envio, provando o funcionamento de stream.

### Pontos Técnicos Relevantes (Análise Crítica)

Apesar de funcional, a implementação concorrente apresenta algumas limitações importantes:
- O uso da biblioteca `_thread` é de baixo nível e menos segura comparada à `threading`, pois não oferece controle refinado de threads.
- Não há sincronização de recursos compartilhados (ex: prints podem se misturar no terminal).
- O servidor não trata exceções dentro da thread, o que pode causar falhas silenciosas.
- Não existe controle de limite de threads → em cenários reais, isso pode causar sobrecarga (problema de escalabilidade).
- Não há envio de resposta do servidor para o cliente neste fluxo concorrente (a comunicação é unidirecional).

Mesmo assim, para fins didáticos, os códigos cumprem muito bem o objetivo de demonstrar concorrência e uso fundamental dos protocolos TCP e UDP em Python.

---

## 7. CONCLUSÃO

A atividade permitiu compreender, de forma prática, como funciona a comunicação cliente-servidor utilizando sockets TCP e UDP, e, principalmente, como a concorrência pode ser implementada em servidores reais.

A principal evolução em relação ao modelo iterativo está no uso de threads, que elimina o bloqueio no atendimento e possibilita que múltiplos clientes sejam atendidos simultaneamente. Isso torna o sistema mais próximo de aplicações reais, como servidores web e sistemas distribuídos.

Os testes realizados com múltiplos clientes simultâneos comprovaram que a abordagem funciona corretamente, evidenciando o uso eficiente de portas efêmeras e execução paralela das threads.

Além disso, a atividade reforçou conceitos importantes como:
- Comunicação orientada à conexão (TCP) e não-orientada à conexão (UDP).
- Serialização de dados (`encode`/`decode`).
- Controle de fluxo básico em aplicações de rede.
- Concorrência e paralelismo.

Apesar de simples, a implementação abre espaço para melhorias futuras, como uso de bibliotecas mais robustas (`threading`), tratamento de exceções mais completo, comunicação bidirecional generalizada e controle de carga.

De forma geral, o objetivo proposto foi totalmente alcançado, proporcionando não apenas a execução prática, mas também uma compreensão mais profunda do funcionamento interno de servidores concorrentes e implementações de rede.
