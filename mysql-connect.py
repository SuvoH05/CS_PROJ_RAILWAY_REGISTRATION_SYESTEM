import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="rrs123",database="Rounak")
if mydb.is_connected():
    print("Connected to the database")
else:
     print("Can not connect to the database")   
mycursor=mydb.cursor()
mycursor.execute("INSERT INTO STUDENT VALUES(125,12,'A',3,'RAM SHARMA',90)")
mycursor.execute("Select * from STUDENT")
for i in mycursor:
    print(i)
mycursor.execute("COMMIT")
mycursor.close()
