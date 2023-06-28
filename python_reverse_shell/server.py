import socket

server_ip = ''  
server_port = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.bind((server_ip, server_port))

sock.listen(1)
print('Server is listinig on port 9999....')

client_socket, client_address = sock.accept()
print('Verbindung hergestellt:', client_address)

while True:
    cmd = input("cmd>>")
    if cmd == "quit-r":
        sock.close()
        break
    client_socket.sendall(cmd.encode())
    data = client_socket.recv(1024)
    print("OUT>>" + data.decode())


