import socket

server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

server_socket.bind(("::", 8080))

server_socket.listen(5)

client_socket, client_address = server_socket.accept()
print(client_socket, client_address)

print("Server bound successful!")
