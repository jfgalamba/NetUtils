"""
Exemplo de um servidor TCP.
"""

from socket import socket, AF_INET, SOCK_STREAM
import threading

BUFFER_DIM = 8192
IP = '0.0.0.0'
PORT = 8888


def main():
    with socket(AF_INET, SOCK_STREAM) as serv_socket:
        serv_socket.bind((IP, PORT))
        serv_socket.listen()

        print(f"[+] Listening on IP {IP} and PORT {PORT}")

        while True:
            client_socket, client_addr = serv_socket.accept()
            print(f"[+] Accepted connection from ({client_addr[0]}, {client_addr[1]})")
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()


def handle_client(client_socket: socket):
    with client_socket:
        request = client_socket.recv(BUFFER_DIM)
        print(f"[+] Client request => {request.decode()}")
        client_socket.send(b'OK')


if __name__ == '__main__':
    main()

