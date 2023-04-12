import socket
import sys
from datetime import datetime

target = input("Enter target")
targetIP = socket.gethostbyname(target)

tstart = datetime.now()

try:
    for p in range(1, 45000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex((targetIP, p))
        if res == 0:
            print("Offener Port: " + str(p))
        sock.close()
except Exception:
    print("There was an erros")
    sys.exit()

tend = datetime.now()
diff = tend - tstart
print("Scan has been teaken " + str(diff))