import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

file_name = input("Enter the name of the file to request: ")
client_socket.sendall(file_name.encode())

file_contents = client_socket.recv(1024).decode()
print(f"Received file contents: {file_contents}")

client_socket.close()
