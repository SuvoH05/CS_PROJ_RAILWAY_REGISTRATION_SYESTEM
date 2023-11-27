import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="2005",database="cs_proj")
if mydb.is_connected():
    print("Connected to the database")
else:
     print("Can not connect to the database")   
myc=mydb.cursor()
myc.execute("drop table if exists login")
myc.execute("create table login (username varchar(30), password varchar(16), primary key (username))")

myc.execute("INSERT INTO login VALUES('SuvoH05','suvo123')")
myc.execute("INSERT INTO login VALUES('MaybeAnkit','ankit1296')")
myc.execute("INSERT INTO login VALUES('Mosa69','dengu69')")
myc.execute("INSERT INTO login VALUES('SuryaFked','fucked24/7')")
myc.execute("INSERT INTO login VALUES('Kiddo','bhau123')")
myc.execute("Select * from login")
for i in myc:
    print(i)
myc.execute("COMMIT")
myc.close()

