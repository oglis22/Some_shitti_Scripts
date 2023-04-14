import tkinter as tk
import socket
import sys
from datetime import datetime

window = tk.Tk()

window.title("PortScanner")
window.geometry("400x400")

label = tk.Label(window, text="PortScanner")
label.config(font=("Arial", 20))
label.pack()

targetIPLabel = tk.Label(window, text="Enter targetIP")
targetIPLabel.pack()

def scanport():
    print("Strat Port scanning")
    tIP = targetIP.get()
    print("target: " + tIP)
    IP = socket.gethostbyname(tIP)

    tstart = datetime.now()

    try:
        for p in range(1, 45000):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            res = sock.connect_ex((targetIP, p))
            if res == 0:
                print("Offener Port: " + str(p))
                p = tk.Label(window, text="Offener Port: " + str(p))
                p.pack()
            sock.close()
    except Exception:
        print("There was an erros")
        sys.exit()

    tend = datetime.now()
    diff = tend - tstart
    print("Scan has been teaken " + str(diff))


targetIP = tk.Entry(window)
targetIP.pack()

button = tk.Button(window, text="Scan Port", command=scanport)
button.pack()


window.mainloop()