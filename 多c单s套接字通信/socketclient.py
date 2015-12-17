#coding:utf-8
import socket
#HOST='192.168.100.12'
PORT=50007
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('192.168.100.12',PORT))      
while 1:
    print "fff"
    a=raw_input("Please input key:")    
    b=raw_input("Please input value:")
    di={a:b}
    wdata=str(di)
    s.sendall(wdata)      #把命令发送给对端
    data=s.recv(8192)     #把接收的数据定义为变量
    print data         #输出变量
s.close()   #关闭连接
