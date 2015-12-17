s='root@cloud_localhost:3306/database'
l=['user','password','hostname','port','databasename']
flagstr=['@','_',':','/']
j=0
for i in flagstr:
       index=s.find(i)
       d=s[:index]
       print l[j]+':'+d
       j=j+1
       s=s[index+1:]
       
print l[-1]+':'+s


