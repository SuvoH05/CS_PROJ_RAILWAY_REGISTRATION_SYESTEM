import random
import string

# Railway Registration System

def login(rand):
    username = input("Enter your Username: ")
    password = input("Enter your Password: ")
    print("captcha: " + str(rand))
    captcha = input("Enter the captcha: ")
    if captcha == rand:
        print("Sucessful login......")
    else:
        print("Wrong Captcha")
        login(rand)

def booking_ticket():
    From = input("Enter from where you want to departure: ")
    To = input("Enter where you want to go: ")
    DMYr = input("Enter date, month adn year as (DD/MM/YYYY): ")
    Classes = input("Enter your preferred class: ")
    Catagory = input("Enter your catagory: ")
    
    
rand = "".join(random.choices(string.ascii_letters + string.digits, k=5))
login(rand)
