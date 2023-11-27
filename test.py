import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="2005",database="cs_proj")
myc=mydb.cursor()
myc.execute("select * from login")
for i in myc:
    print(i)

myc.close()