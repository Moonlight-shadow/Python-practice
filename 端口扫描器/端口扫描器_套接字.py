#!/usr/bin/env python#!/usr/bin/env python
# -*- coding: utf8 -*-
import telnetlib
import threading,time,socket
l=[]
hostname=raw_input('请输入要扫描的ip地址:')
#hostname='172.16.0.11'     #替换成实际ip地址        
def scan(port):
		  try:
			s = socket.socket() 
			s.connect((hostname,port))
		  	l.append(port)
			s.close()
		  
		  except:
			pass
def main():
	start=time.time()
	for port in range(1,65535):		#括号里面为端口范围1-65536，但windows只支持同时开2000个(实际测试中最大只能868，可能是系统本身有占用一些)，建议用linux则不会有问题
		t = threading.Thread(target=scan,args=(port,))
		t.setDaemon(True)
		t.start()
		#time.sleep(0.001)
	stop=time.time()
	print ('本次扫描一共花费%s秒' %(stop-start))
	print ('%s有以下端口正在提供服务'%(hostname))
	for i in l:  
		print i
if __name__=='__main__':  
    main()  
