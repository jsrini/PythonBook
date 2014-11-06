import socket
import threading

class Client(threading.Thread):
    def __init__(self, clientsock, address):
        threading.Thread.__init__(self)
        self.clientsock = clientsock
        self.address = address

    def run(self):
        done = False
        while not done:
           data = self.clientsock.recv(size)
           data = data.decode('utf-8')
           if data == 'Exit':
               done = True
               done = True
           outstr = '*** '+data
           self.clientsock.send(outstr.encode('utf-8'))
        self.clientsock.close()

host = 'localhost'
port = 2000
size = 512

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM)

sock.bind(('',port))
sock.listen(5)
while True:
    clientsock, address = sock.accept()
    clientthread = Client(clientsock,address)
    clientthread.start()