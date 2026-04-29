# Relatório de Execução: Sockets TCP Concorrentes em Python

Este documento detalha a implementação e os testes realizados para validar a comunicação multiponto utilizando Sockets TCP e Threads em Python.

---

## 🚀 Demonstração da Execução (Capturas de Tela)

Abaixo estão registradas as evidências de funcionamento do sistema com três clientes simultâneos e o servidor processando todas as requisições.

### 💻 Clientes em Execução
Cada cliente opera em um terminal independente, enviando mensagens únicas para o servidor.

| Cliente 1 | Cliente 2 | Cliente 3 |
| :---: | :---: | :---: |
| ![Mensagem Cliente 1](cliente1.png) | ![Mensagem Cliente 2](cliente2.png) | ![Mensagem Cliente 3](cliente3.png) |
| *Envio de mensagem inicial* | *Teste de concorrência* | *Validação de terceira via* |

---

### 🖥️ Visão Geral do Servidor
O terminal do servidor centraliza o recebimento de todas as mensagens, identificando cada cliente por sua porta efêmera única.

![Terminal do Servidor](servidor.png)
*Legenda: Servidor processando mensagens de múltiplos IDs de threads simultaneamente.*

---

## 🛠️ Detalhes da Implementação

### 1. Servidor Concorrente (`sockete_tcp_concorrente_servidor.py`)
O servidor utiliza a biblioteca `_thread` para garantir que o loop principal não seja bloqueado.
*   **Endereço:** `127.0.0.1` (Localhost)
*   **Porta:** `50000`
*   **Capacidade:** Configurado com `tcp.listen(5)` para gerenciar a fila de espera.

### 2. Cliente TCP (`socket_tcp_concorrente_cliente.py`)
O cliente foi ajustado para conectar-se ao endereço de loopback, garantindo que o teste funcione em ambiente local.
*   **Protocolo:** TCP (Stream)
*   **Saída:** Implementada verificação de mensagem vazia ou `CTRL+X` para encerramento seguro da conexão.

---

## 🧠 Explicação Técnica
O teste valida o conceito de **Servidor Concorrente**. Diferente de um servidor iterativo (que atende um por um), este modelo cria um "espaço de trabalho" (Thread) dedicado para cada conexão. 

**Por que mudar para 127.0.0.1?**
Conforme solicitado pelo professor, a alteração é necessária pois o código original pode conter IPs de redes externas. O IP `127.0.0.1` garante que o tráfego de rede nunca saia da placa de rede local, permitindo o teste mesmo sem conexão externa.

---
*Relatório gerado para a disciplina de Redes de Computadores.*
