"""
4. Create an online shipping system with the following features:
* 		The system has a login that locks after the third failed attempt.
* 		Display a menu that allows: Sending a package, exiting the system.
* 		To send a package, sender and recipient details are required.
* 		The system assigns a random package number to each sent package.
* 		The system calculates the shipping price. $2 per kg.
* 		The user must input the total weight of their package, and the system should display the amount to pay.
* 		The system should ask if the user wants to perform another operation. If the answer is yes, it should return to the main menu. If it's no, it should close the system.
"""

from random import randrange

def user_singup():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    if password == confirm_password:
        print("You have sucesfuly sing up \n")
        user = [username,password]
    else:
        print("The passwords doesn't match. ")
    return user

def user_login(user,password,data_user):
    attempts = 0
    while attempts <= 3:
        if user == data_user[0] and password == data_user[1]:
            message = "You have succesfuly log in. "
            break
        else:
            print("Wrong username or password. Try again")
            user = input("Enter your user name: ")
            password = input("Enter your password: ")
        attempts += 1
        if attempts == 3: 
            message = "Your account was locked due to too many failed attempts."
            break
    return message

def menu():
    print("WELCOME TO THE ONLINE SHIPPING SYSTEM")
    print("1- Sending a package")
    print("2- Exiting the system")
    choice = input("Enter the number (1 or 2) depending of what you want to do: ")
    return "You has selected the option " + choice

def send_package():
    sender_details = input("\nEnter the sender's first name: ") 
    address_sender = input("Enter the sender's address: ")
    reciever_details = input("Enter the recipient's first name: ")
    address_reciever = input("Enter ther reciever's address: ")
    weight = float(input("Enter the weight of the package in kilograms: "))
    number_package = randrange(0,10000,2) 
    print("\nThe number of the package is " + str(number_package))
    package = [sender_details, address_sender, reciever_details, address_reciever, weight, number_package]
    return package 

print("ONLINE SHIPPING SYSTEM \n")
account = input("Do you already have an account? (Y/n): ").upper()
if account == 'Y':
    username = input("Enter your username: ").capitalize()
    password = input("Enter your password: ").capitalize()
    user1 = ['Francisco', 'Tato']
    login_message = user_login(username,password,user1)
    print(login_message)
    if login_message == "You have succesfuly log in. ":
        menu = menu()
        print(menu)
        if menu == "You has selected the option 1":
            data = send_package()
            price = float(data[4]) * 2
            print("The weight in kg is " + str(data[4]) + " and the total price is " + str(price))
            print("\nThank you for use the Online Shipping System. \n")
            choice = input("Do you want to do another opeartion?(Y/n): ").upper()
            if choice == "Y":
                data = send_package()
                price = float(data[4]) * 2
                print("The weight in kg is " + str(data[4]) + " and the total price is " + str(price))
                print("\nThank you for use the Online Shipping System. \n")
            else:
                print("The system will shut down. Thank you for using the Online Shipping System!!!!. ")
        elif menu == "You has selected the option 2":
            print("The system will shut down. Thank you for using the Online Shipping System!!!!. ")
        else:
            print("Invalid Option! Try again.")
    else:
       print("Wrong credentials. Try again. ")
elif account == 'N':
   user = user_singup()
   print("New User Account Created!. Please Log in to continue: ")
   username = input("Enter your username: ")
   password = input("Enter your password: ")
   user1 = [user[0],user[1]]
   login_message = user_login(username,password,user1)
   print(login_message)
   if login_message == "You have succesfuly log in. ":
        menu = menu()
        print(menu)
        if menu == "You has selected the option 1":
            data = send_package()
            price = float(data[4]) * 2
            print("The weight in kg is " + str(data[4]) + " and the total price is " + str(price))
            print("\nThank you for use the Online Shipping System. \n")
            choice = input("Do you want to do another opeartion?(Y/n): ").upper()
            if choice == "Y":
                data = send_package()
                price = float(data[4]) * 2
                print("The weight in kg is " + str(data[4]) + " and the total price is " + str(price))
                print("\nThank you for use the Online Shipping System. \n")
            else:
                print("The system will shut down. Thank you for using the Online Shipping System!!!!. ")
        elif menu == "You has selected the option 2":
            print("The system will shut down. Thank you for using the Online Shipping System!!!!. ")
        else:
            print("Invalid Option! Try again.")
   else:
       print("Wrong credentials. Try again. ")



    