import socket

server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

server_socket.bind(("::", 8080))
print("Server bound successful!", server_socket)

server_socket.listen(5)

client_socket, client_address = server_socket.accept()
print(f"Client Connected :{client_address}")

data = client_socket.recv(1024)
print(f"Data Received :{data}")

send_data = "Hey, I sent you this.".encode() #output : b"Hey, I sent you this."
client_socket.sendall(send_data)
print("Data sent successfully!")

client_socket.close()
server_socket.close()

