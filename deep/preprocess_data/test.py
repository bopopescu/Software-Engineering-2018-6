filepath = 'list_attr_cloth.txt'  
f=open('classs.txt', 'w')
with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   class1 = []
   while line:
       #print("{}: {}".format(cnt, line.strip()))
       row=line.find(str(5))
       if(row>0):
           time=str(cnt-1)
           print(time.rjust(3),":",line.strip())
           liii=time.rjust(3)+":"+line.strip()
       line = fp.readline()
       cnt += 1
