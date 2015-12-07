#!/usr/bin/env python
#coding:utf-8
import commands

def getsizedir(dirname):
    message=None
    status=-1
    cmd = " df "+dirname +" | awk '{print $3 \" \" $4}'"
    if type(dirname) == str:
        status,message = commands.getstatusoutput(cmd)
    
        usedv = message.split("\n")[1].split(" ")[0]
        Availv = message.split("\n")[1].split(" ")[1]
        dicmessage={'used':usedv,'Available':Availv}
        print dicmessage
    return status,message

if __name__ == '__main__':
    status,message = getsizedir('/home')
    print  status
