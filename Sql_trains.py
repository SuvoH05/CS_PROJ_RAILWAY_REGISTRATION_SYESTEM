import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="2005",database="cs_proj")
if mydb.is_connected():
    print("Connected to the database")
else:
     print("Can not connect to the database")   
myc=mydb.cursor()
#myc.execute("drop table if exists trains")
myc.execute("create table trains (TrainNo int, `From` varchar(30), `To` varchar(16), DMYr varchar(11), Classes varchar(20), Catagory varchar(20), primary key (TrainNo))")
n= int(input("Enter no of records you want to enter:" ))
for i in range(n):
    TrainNo = int(input("Enter train number: "))
    From = input("Enter from where you want to departure: ")
    To = input("Enter where you want to go: ")
    DMYr = input("Enter date, month adn year as (DD/MM/YYYY): ")
    Classes = input("Enter your preferred class: ")
    Catagory = input("Enter your catagory: ")
    info = "INSERT INTO trains VALUES({},'{}','{}','{}','{}','{}')".format(TrainNo,From,To,DMYr,Classes,Catagory)
    myc.execute(info)

myc.execute("Select * from trains")

for i in myc:
    print(i)

myc.execute("COMMIT")
myc.close()

