# client.py  
import socket
import os

def encode_dir(path):    
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".pd"):
                print(os.path.join(root, file))

encode_dir("../../testing/cosc469-testing-data")


# # create a socket object
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# # get local machine name
# host = socket.gethostname()                           

# port = 9999

# # connection to hostname on the port.
# s.connect((host, port))                               

# # Receive no more than 1024 bytes
# tm = s.recv(1024)                                     
# print(tm.decode('ascii'))

# s.close()
