import socket
import pickle

class Network:
    #send [(from),(To)]
    def __init__(self):
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.port=5050
        self.ServerAddress=socket.gethostbyname(socket.gethostname()) # this will get the local server.
        #self.ServerAddress="192.168.1.101"
        print("initializating now")
        #self.ID=self.connect()
        self.connect()
    def connect(self):
        self.client.connect((self.ServerAddress,self.port))
        print("client is trying to connect")
        #a=int(self.receive())
        #print(a)
        #return a
    def disconnect(self):
        self.client.send("!disconnect".encode())
        self.client.close()
    def send(self,data):
        data_string = pickle.dumps(data)#sender no need to calculate the size
        print("sending data")
        print(data)
        self.client.send(data_string)
        print(pickle.loads(data_string))
    def receiveID(self):
        data=self.client.recv(4096)
        return data
    def receive(self):
        data=self.client.recv(4096)
        return pickle.loads(data) # bug bug bug


if __name__ == "__main__":
    n=Network()
    while True:
        print("hi i am the client")

    
        data=n.receive()
        print(data)
    #n.send({0:[(1,2),(2,3)]})
    #n.disconnect()
