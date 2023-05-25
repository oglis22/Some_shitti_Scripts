import socket

def bypass_proxy(target_host, target_port, proxy_host, proxy_port):
    # Erzeuge ein Socket-Objekt und stelle eine Verbindung zum Proxy her
    proxy_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_socket.connect((proxy_host, proxy_port))

    # Sende eine CONNECT-Anfrage an den Proxy, um eine direkte Verbindung zum Ziel herzustellen
    connect_request = f"CONNECT {target_host}:{target_port} HTTP/1.1\r\nHost: {target_host}\r\n\r\n"
    proxy_socket.send(connect_request.encode())

    # Empfange die Antwort des Proxys
    response = b""
    while b"\r\n\r\n" not in response:
        response += proxy_socket.recv(4096)

    # Überprüfe, ob die Verbindung erfolgreich hergestellt wurde
    if b"200 Connection established" in response:
        print("Direkte Verbindung hergestellt. Bypass erfolgreich!")
        
        # Verbinde dich direkt mit dem Ziel
        target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        target_socket.connect((target_host, target_port))
        
        # Leite den Datenverkehr zwischen Proxy und Ziel weiter
        while True:
            # Empfange Daten vom Proxy
            proxy_data = proxy_socket.recv(4096)
            if not proxy_data:
                break
            
            # Sende Daten an das Ziel
            target_socket.sendall(proxy_data)
            
            # Empfange Daten vom Ziel
            target_data = target_socket.recv(4096)
            if not target_data:
                break
            
            # Sende Daten an den Proxy
            proxy_socket.sendall(target_data)
        
        # Schließe die Verbindungen
        target_socket.close()
        proxy_socket.close()
    else:
        print("Bypass fehlgeschlagen. Proxy antwortete nicht wie erwartet.")

# Beispielaufruf
bypass_proxy("example.com", 80, "proxy.example.com", 8080)
