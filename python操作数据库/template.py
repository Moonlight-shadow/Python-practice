#/usr/bin/env python 
#coding:utf-8
import MySQLdb
import traceback
class mySqlConn(object):
    def __init__(self,passwd,user='root',host='localhost',port=3306):
        self.passwd=passwd
        self.db="nodes"
        self.host=host
        self.port=port
        self.user=user
        self.conn=None
        self.cursor=None
    def connect(self):
        if not self.conn:
                self.conn=MySQLdb.connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,port=self.port)
    def close(self):
        if not self.conn:
            self.conn.close()
        self.conn=None
    def addcapacity(self,*argv):
        return self.template(self.addCapacityExec,*argv)
        
    def addCapacityExec(self,ip,avai,used):
        sql="insert into capacity(ip,avai,used) values(\'%s\',%d,%d)"%(ip,avai,used)
        self.cursor.execute(sql)

    def template(self,fun,*argv):
        result=None
        self.connect()
        try:
            self.cursor=self.conn.cursor()
            result=fun(*argv)
            self.conn.commit()
        except:
            traceback.print_exc()
            self.conn.rollback()
        if not self.cursor:
            self.cursor.close()
        self.close()
        return result
    def CapacityQuery(self,*argv):
        return self.template(self.CapacityQueryExec,*argv)
    def CapacityQueryExec(self,ip):
        sql="select id,avai,used from capacity where ip=\'%s\'"%(ip)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        for row in results:
            idnum = row[0]
            avai = row[1]
            used = row[2]
        print "id=%d,avai=%d,used=%d"%(idnum,avai,used)
    def CapacityRefrensh(self,*argv):
        return self.template(self.CapacityRefrenshExex,*argv)
    def CapacityRefrenshExex(self,ip,avai,used):
        sql="update capacity  set avai=%d,used=%d where ip=\'%s\'"%(avai,used,ip)
        self.cursor.execute(sql)
    def NewFiles(self,*argv):
        return self.template(self.NewFilesExex,*argv)
    def NewFilesExex(self,hostid,filename):
        sql="insert into files(hostid,filename) values(%d,\'%s\')"%(hostid,filename)
        self.cursor.execute(sql)
    def Settingsize(self,*argv):
        return self.template(self.SettingsizeExec,*argv)
    def SettingsizeExec(self,size,hostid,files):
        sql="update files set size=%d where hostid=%d and filename=\'%s\'"%(size,hostid,files)
        self.cursor.execute(sql)
    def FilenameSIp(self,*argv):
        return self.template(self.FilenameSIpExec,*argv)
    def FilenameSIpExec(self,filename):
        sql="select capacity.ip from capacity,files where filename=\'%s\'"%(filename)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        for row in results:
            ip= row[0]
        print "ip=%s"%ip
if __name__=="__main__":
    sconn=mySqlConn("cloud",host="192.168.100.51")
    #sconn.addcapacity("21",54,14)
    #sconn.CapacityQuery('1')
    #sconn.CapacityRefrensh('1',111,20)
    #sconn.NewFiles(8,'zdfdf')
    #sconn.Settingsize(20,1,'zdff')
    sconn.FilenameSIp('zdff')
