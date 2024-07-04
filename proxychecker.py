import requests
import time
import threading
import queue

def checkProxy():
    global q
    proxy = q.get()
    try:
        resp = requests.get("http://ipinfo.io/json", proxies={
            "http": proxy,
            "https": proxy
        })

        if resp.status_code == 200:
            print(proxy)
    except: 
        pass

def main():
    global q
    while not q.empty():
        checkProxy()
        time.sleep(0.5)


if __name__ == "__main__":

    q = queue.Queue()

    with open("proxies.txt", "r") as p:
        pr = p.read().split("\n")
        for p in pr:
            q.put(p)

    for _ in range(10):
        threading.Thread(target=main).start()
        


