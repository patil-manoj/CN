import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))

while True:
    data, client_address = server_socket.recvfrom(1024)
    file_name = data.decode()
    print(f"Received file name: {file_name}")

    try:
        with open(file_name, 'r') as f:
            file_contents = f.read()
            server_socket.sendto(file_contents.encode(), client_address)
            print(f"Sent file contents")
    except FileNotFoundError:
        server_socket.sendto(b"File not found", client_address)
        print(f"Sent 'File not found' message")
