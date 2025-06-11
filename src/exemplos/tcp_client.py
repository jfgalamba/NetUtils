"""
Exemplo de um cliente TCP.
"""

from socket import socket, AF_INET, SOCK_STREAM

target_host = "127.0.0.1"
target_port = 8888        # porto para acesso HTTP

# target_host = "www.google.com"
# target_port = 80        # porto para acesso HTTP

# Criar objecto socket
# AF_INET -> Internet, IPv4 |  SOCK_STREAM -> TCP (orientado ao byte)
client_socket = socket(AF_INET, SOCK_STREAM)

# Ligar ao servidor
client_socket.connect((target_host, target_port))

# Enviar pedido/método GET
request = b'GET / HTTP/1.1\r\nHost: google.com\r\n\r\n'
"""
O request corresponde a um "pacote" HTTP. Se fizermos um print do request 
obtemos:
    GET / HTTP/1.1 
    Host: google.com
"""
client_socket.send(request)

# Aguarda por uma resposta (e reserva um buffer com 8192 bytes para essa resposta)
response = client_socket.recv(8192)

print(response.decode())
client_socket.close()   # na verdade devemos abrir o socket com WITH e nesse
                        # caso o close é feito sempre que o bloco do WITH terminar

