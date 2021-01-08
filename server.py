import socket
import threading
import time
import pickle

PORT=5050   #1024-65535
DISCONNECTMESSAGE="!disconnect"
SERVER=socket.gethostbyname(socket.gethostname()) # local ip address , we get it by use DNS lookup table
#SERVER="192.168.1.101"
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # socket with type ip4,  socket stream is the type as well.
# this are int value so u dont have to code yourself. 
#it return the socket descriptor 
ADDR=(SERVER,PORT)

server.bind(ADDR) # match port number to this socket,so package directed to this port will be given to this socket 

BoardData=None
chessPlayer=[] # for now it only accept two player
def handle_client(socketNumber,address,ID):
    print(address,"player connected")
    connected=True
    while connected:
        data=socketNumber.recv(4098) # input is the maximum amount of data to be received. return value is bytes object representating data received.
        if data:
            chessPlayer[(1+ID)%2].send(data)
            print(pickle.loads(data))
        
    socketNumber.close()

counter=0
def start():
    global counter
    print("server started running, address is ",SERVER)
    server.listen() # server is listening to this port
    while True:
        clientSocketNumber,addr=server.accept() #u have two socket file descriptors for the price of one! the orignal one is still listening for connection. 
#return port and ip address
        # this code will wait to accept , then it will execute 
        if len(chessPlayer)<3:
            chessPlayer.append(clientSocketNumber)
            if len(chessPlayer)==2:
                for i in range(len(chessPlayer)):
                    chessPlayer[i].send(str(i).encode())
            thread=threading.Thread(target=handle_client,args=(clientSocketNumber,addr,counter))
            thread.start()
            counter+=1
            print(counter)
            print("active connection",threading.activeCount()-1)
start()