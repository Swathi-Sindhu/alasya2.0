import sqlite3

db=sqlite3.connect("data")


c=db.cursor()
c.execute("SELECT * FROM contacts")
for i,j,k,l in c: 
 print(i)
 print(j)
 print(k)
 print(l)
 print('-'*20)
 

c.close()
db.commit()
db.close()

