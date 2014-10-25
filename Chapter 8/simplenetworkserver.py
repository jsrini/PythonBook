import socket

host = 'localhost'
port = 2000
size=512

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('',port))
sock.listen(5)
while True:
    clientsock, address = sock.accept()
    done=False
    while done==False:
        data = clientsock.recv(size)
        data= data.decode('utf-8')
        if data == 'Exit':
            done=True
        outstr='*** '+data
        clientsock.send(outstr.encode('utf-8'))
        
        

