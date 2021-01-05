import socket
import threading
import time

PORT=5050   #1024-65535
DISCONNECTMESSAGE="!disconnect"
SERVER=socket.gethostbyname(socket.gethostname()) # local ip address , we get it by use DNS lookup table
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # socket with type ip4,  socket stream is the type as well.
# this are int value so u dont have to code yourself. 
#it return the socket descriptor 
ADDR=(SERVER,PORT)

server.bind(ADDR) # match port number to this socket,so package directed to this port will be given to this socket 

def handle_client(socketNumber,address):
    print(address,"connected")
    connected=True
    while connected:
        msg=socketNumber.recv().decode("utf-8") # input is the maximum amount of data to be received. return value is bytes object representating data received. 
        if msg==DISCONNECTMESSAGE:
            connected=False
        print(msg)
    socketNumber.close()
        

def start():
    server.listen() # server is listening to this port
    while True:
        clientSocketNumber,addr=server.accept() #u have two socket file descriptors for the price of one! the orignal one is still listening for connection. 
#return port and ip address
        thread=threading.Thread(target=handle_client,args=(clientSocketNumber,addr))
print(SERVER)