#coding:utf-8
"""创建线程，接受从socket客户端发过来的字符串"""
import threading
class mythread(threading.Thread):
    def __init__(self,conn,addr):
        threading.Thread.__init__(self)
        self.conn=conn
        self.addr=addr
    def run(self):
        rdata=self.conn.recv(8192)
        if type(rdata)!=dict:
            try:
                dicrdata=None
                exec("dicrdata="+rdata)
                print dicrdata
            except  SyntaxError:
                dicrdata=None
        print "That's Ok"
        self.conn.close()
     
