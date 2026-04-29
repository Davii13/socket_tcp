import socket

HOST = '127.0.0.1' # Endereco IP do Servidor
PORT = 50000 # Porta que o Servidor está

# Criando a conexão
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)

try:
    tcp.connect(destino)
    print('\nDigite suas mensagens')
    print('Para sair use CTRL+X e Enter (ou apenas Enter vazio se o loop permitir)\n')
    
    while True:
        # Recebendo a mensagem do usuário final pelo teclado
        mensagem = input('Sua mensagem: ')
        
        # Enviando a mensagem para o Servidor TCP através da conexão
        # No Windows, input() não captura CTRL+X facilmente como caractere \x18 
        # a menos que o terminal suporte. Vamos usar um Enter vazio ou string 'sair' como fallback.
        if mensagem == '\x18' or mensagem.lower() == 'sair' or not mensagem:
            break
            
        tcp.send(mensagem.encode())
        
except Exception as e:
    print(f'\nErro: {e}')
finally:
    # Fechando o Socket
    print('\nFechando conexão...')
    tcp.close()