import socket
import os

def serve_file(client_socket, file_path):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            client_socket.sendall(data)
    except IOError:
        client_socket.sendall(b'File not found')

def handle_client(client_socket):
    file_name = client_socket.recv(1024).decode('utf-8')
    file_path = os.path.join('files', file_name)

    if os.path.isfile(file_path):
        client_socket.sendall(b'OK')
        serve_file(client_socket, file_path)
    else:
        client_socket.sendall(b'File not found')

    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8888))
    server_socket.listen(5)
    print('Server listening on port 8888...')

    while True:
        client_socket, addr = server_socket.accept()
        print('Connected to', addr)
        handle_client(client_socket)

start_server()
