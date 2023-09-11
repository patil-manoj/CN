import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

file_name = input("Enter the name of the file to request: ")
client_socket.sendto(file_name.encode(), ('localhost', 12345))

data, _ = client_socket.recvfrom(1024)
file_contents = data.decode()
print(f"Received file contents: {file_contents}")

client_socket.close()
