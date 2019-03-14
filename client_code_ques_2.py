import socket
host='128.104.159.143'
port=1993
s=socket.socket()
s.connect((host,port))
f=raw_input("Please enter-->")
g=open('sai.txt','rb')
n=g.read()
while True:
        if f=='exit':
                s.send(f)
                data=s.recv(102400)
                print str(data)
                break
        else:
                s.send(n)
                data=s.recv(102400)
                print str(data)
                f=raw_input()
s.close()
