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

    data_received = client_socket.recv(1024)
    print(f"Data Received :{data_received}")

    data_received_decoded = data_received.decode()
    data = data_received_decoded.split("\r\n")
    parse_request = data[0].split()
    print(parse_request)


    #send_data = "Hey, I sent you this.".encode() #output : b"Hey, I sent you this."
    body = "<h1>Hello from Server<h1>"
    body_bytes = body.encode()
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type:text/html\r\n"
        f"Content-Length:{len(body_bytes)}\r\n"
        "\r\n"
        f"{body}"
    )
    client_socket.sendall(response.encode())
    print("Data sent successfully!")

    client_socket.close()

#server_socket.close()

