#!/usr/bin/env python

import socket

 
TCP_IP = '192.168.0.160'
TCP_PORT = 4445
BUFFER_SIZE = 1024
MESSAGE = 'Hello, World!\n'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode())
rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rs.bind(('', 4444))
rs.listen(1)
conn, addr = rs.accept()
print ('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("received data:", data.decode())
conn.close()
rs.close()
s.close()