import socket

PORT=5050
DISCONNECTMESSAGE="!disconnect"
SERVER="127.0.0.1"
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ADDR=(SERVER,PORT)
client.connect(ADDR)

def send(msg):
    message=msg.encode("utf-8")
    