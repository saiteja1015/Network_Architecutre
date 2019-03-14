import socket
host=socket.gethostbyname("128.104.159.143")
port=5000
s=socket.socket()
s.connect((host,port))
message=raw_input("enter -->")
while True:
        if message == 'Bye from Client- Sai':
                s.send(message)
                data=s.recv(1024)
                print str(data)
                break
                message=raw_input()
        elif message == 'Hello from Client- Sai':
                s.send(message)
                data=s.recv(1024)
                print str(data)
                message=raw_input()
        else:
                s.send(message)
                data=s.recv(1024)
                print str(data)
s.close()
