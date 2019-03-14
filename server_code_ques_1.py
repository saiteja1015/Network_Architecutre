import socket
host=socket.gethostbyname("128.104.159.143")
port=5000
s=socket.socket()
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
while True:
        data=c.recv(1024)
        if data=='Bye from Client- Sai':
                c.send('Bye from Server- Sai')
                break
        elif data=='Hello from Client- Sai':
                print str(data)
                c.send('Hello from Server- Sai')
        else:
                print str(data)
                c.send(data)
c.close()
