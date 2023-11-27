import random
import string
import mysql.connector
# Railway Registration System

def login(rand,Sql):
    username = input("Enter your Username: ")
    password = input("Enter your Password: ")
    print("captcha: " + str(rand))
    captcha = input("Enter the captcha: ")
    if captcha == rand:
        Sql.execute("select * from login")
        for i in Sql:
            if i[0] == username and i[1] == password :
                print ("Login Successful")
            else:
                print ("Invalid Login Details")
                break
    else:
        print("Wrong Captcha")
        login(rand,myc)

def booking_ticket():
    From = input("Enter from where you want to departure: ")
    To = input("Enter where you want to go: ")
    DMYr = input("Enter date, month adn year as (DD/MM/YYYY): ")
    Classes = input("Enter your preferred class: ")
    Catagory = input("Enter your catagory: ")
    
mydb=mysql.connector.connect(host="localhost",user="root",password="2005",database="cs_proj")
rand = "".join(random.choices(string.ascii_letters + string.digits, k=5))
myc=mydb.cursor()

#login(rand,myc)
booking_ticket()