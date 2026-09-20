import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("0.0.0.0", 8080))

# server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# server_socket.bind(("::", 8080))
print("Server bound successful!", server_socket)

server_socket.listen(5)
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Client Connected :{client_address}")

    data = client_socket.recv(1024)
    print(f"Data Received :{data}")

    #send_data = "Hey, I sent you this.".encode() #output : b"Hey, I sent you this."
    body = "<h1>Hello from Server<h1>"
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type:text/html\r\n"
        f"Content-Length:{len(body.encode())}\r\n"
        "\r\n"
        f"{body}"
    )
    client_socket.sendall(response.encode())
    print("Data sent successfully!")

    client_socket.close()
    
server_socket.close()

