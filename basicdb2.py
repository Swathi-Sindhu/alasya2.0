import pymysql

db=pymysql.connect("sql12.freemysqlhosting.net","sql12225454","ZhjfPu9eAU","sql12225454")
a=0;k=0
p=db.cursor()

u=input("Enter your name:");
p.execute("SELECT name1,name2 FROM contacts")
c=p.fetchall()
for i,j in c:
 if(u==j):
  v=i
  break
p.close()

p=db.cursor()
p.execute("SELECT text2,text1 FROM contacts")
c=p.fetchall()
#print(c)
for i,j in c:
 if(i==''):
  print(j)
 if(j==''):
  print(' '*40,end='')
  print(i)
p.close() 
while(a!=1):
 c=db.cursor()
 c.execute("SELECT * FROM contacts")
 if(k!=0):
  c.execute("INSERT INTO contacts (name1,name2,text2,text1) VALUES('" + u + "','" + v + "','" + q + "',' ');")
  c.execute("SELECT text2,text1 FROM contacts")
  z=c.fetchall()
  for i,j in z:
   x=i
  print(' '*40,end='') 
  print(x)
 c.close()
 db.commit()
 print("Enter the text:",end=' ')
 q=input()
 print('\b'*15)
 k+=1

db.close()






