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
        Sql.execute("select * from registration")
        for i in Sql:
            if i[0] == username and i[6] == password :
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
    
def registration(myc):
    Username = input("Enter Your Name: ")
    age = int(input("Enter Your Age: "))
    gender = input("Enter Your Gender: ")
    address = input("Enter Your Address: ")
    contact = int(input("Enter Your Contact Number: "))
    email = input("Enter Your Email ID: ")
    password = input("Enter a strong password: ")
    confirm_pass = input("Confirm Password: ")

    if password != confirm_pass:   
        print("Passwords do not match.")
        password = input("Re-enter new password: ")
        confirm_pass = input("Re-confirm password: ")
    elif len(password)<8 or len(password)>30:
        print("Password should be between 8 and 30 characters long.")
        password = input("Re-enter new password: ")
        confirm_pass = input("Re-confirm password: ")
        
    info = "INSERT INTO registration VALUES('{}',{},'{}','{}',{},'{}','{}')".format(Username,age,gender,address,contact,email,password)
    myc.execute(info)
    myc.execute("commit")
        


mydb=mysql.connector.connect(host="localhost",user="root",password="2005",database="cs_proj")
rand = "".join(random.choices(string.ascii_letters + string.digits, k=5))
myc=mydb.cursor()
login(rand,myc)
#booking_ticket()
#registration(myc)
