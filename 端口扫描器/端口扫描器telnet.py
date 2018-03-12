import telnetlib
import threading,time
l=[]
def scan(port):
		  try:
		  	p=telnetlib.Telnet('172.16.0.15',port)
		  	l.append(port)
		  
		  except:
			pass
def main():
	start=time.time()
	for port in range(1,65535):
		t = threading.Thread(target=scan,args=(port,))
		t.start()
	stop=time.time()
	print stop-start
	for i in l:  
		print i
if __name__=='__main__':  
    main()  
