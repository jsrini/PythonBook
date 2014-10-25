import socket
import ssl
import pprint

host = 'localhost'
port = 2000
size=512

data=input("Show server certificate? (Y/N)")
if data=='Y' or 'y':
    print(ssl.get_server_certificate((host,port)))



sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.set_ciphers("DH:DSS:AES256:SHA")
securesock = context.wrap_socket(sock)


securesock.connect((host,port))


done = False
while done==False:
    data=input('Enter string: ')
    if data=='Exit':
        done=True
    securesock.send(data.encode('utf-8'))
    data = securesock.recv(size)
    print('Received: '+data.decode('utf-8'))
    
securesock.close()
