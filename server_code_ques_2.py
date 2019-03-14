import socket
import os
host='128.104.159.143'
port=1993
s=socket.socket()
s.bind((host,port))
s.listen(1)
c,addr=s.accept()
while True:
        data=c.recv(102400)
        if data=='exit':
                c.send('server gone')
                break
        else:
                k=open('sai.txt','w')
                k.write(data)
                k.close()
                print str(data)
                c.send(data+'\nAdded By the Server')
c.close()
