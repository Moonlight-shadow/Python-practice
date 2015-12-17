
#!/usr/bin/env python
#coding:utf-8
"""socket服务端，接收数据，增加一个连接创建一个进程，把接收到的数据交给创建的进程处理"""
import socket   
from Theada import mythread
HOST='192.168.100.12'
PORT=50007
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
s.bind((HOST,PORT)) 
s.listen(100)         
while 1:
    conn,addr=s.accept()
    print'Connected by',addr    
    Tc=mythread(conn,addr)
    Tc.start()
conn.close()    
