import socket
import threading
import ssl

class Client(threading.Thread):
    def __init__(self, clientsock, address):
        threading.Thread.__init__(self)
        self.clientsock = clientsock
        self.address = address

    def run(self):
        done = False
        while done == False:
            data = self.clientsock.recv(size)
            data = data.decode('utf-8')
            if data == 'Exit':
                done = True
            outstr = '*** '+ data
            self.clientsock.send(outstr.encode('utf-8'))
        self.clientsock.close()

host = 'localhost'
port = 2000
size = 512

# create TLS context, load certificate
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.set_ciphers("DH:DSS:AES256:SHA")
context.load_cert_chain(certfile="certificate.pem",
                        keyfile="key.pem")


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('',port))
sock.listen(5)
while True:
    clientsock, address = sock.accept()
    securesock = context.wrap_socket(clientsock,
                                     server_side=True)
    clientthread = Client(securesock,address)
    clientthread.start()