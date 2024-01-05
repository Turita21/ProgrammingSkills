"""Create an online banking system with the following features:

* Users must be able to log in with a username and password.
* If the user enters the wrong credentials three times, the system must lock them out.
* The initial balance in the bank account is $2000.
* The system must allow users to deposit, withdraw, view, and transfer money.
* The system must display a menu for users to perform transactions."""


print("Online banking system")

print("Do you have an account already?")
print("To login enter 's'.")
print("To sign up enter 'n'.")
option = input()

if option == "s":
    user_name = input("Introduce your user name: ")
    password = input("Introduce your password: ")

if option == "n":
    name = input("Please introduce your name: ")
    user = input("Please create an user: ")
    mail = input("Please introduce your email: ")
    passw = input("Please create a password: ")
    print("\nYour data has been registered.\n\nNow you can login.")
    lists = []
    lists.append(name)
    lists.append(user)
    lists.append(mail)
    lists.append(passw)
    user_name = input("Introduce your user name: ")
    password = input("Introduce your password: ")
else:
    print("The option is incorrect. Try again. ")


count = 3

def validate_credentials(user_name,password,lists):
    if (user_name == lists[1] and password == lists[3]):
        return True
    return False 



def validate_user(user,lists):
    val = 0
    while val < len(lists):
        users = lists[val]
        if user == users:
            return True
        val = val + 1
    return False    
users = ["Maria", "Juan", "Valeria", "Coral"]

if validate_credentials(user_name, password, lists):
    print("You have successfully logged in.")
    balance = 2000
    print("Welcome to your account, ", user_name)
    print("What transactions do you want to do (Introduce the number of your choice): ")
    print("1) View")
    print("2) Deposit")
    print("3) Transfer")
    print("4) Withdraw")
    choice = input()
    if choice == "1":
        print("Your balance is ",balance )
    elif choice == "2":
        amount=float(input("How much money would you like to deposit? "))
        balance +=amount
        print("Your balance now is: ", balance)
    elif choice == "3":
        user = input("Enter the name of the user you want to deposite to: ").capitalize()
        if validate_user(user,users):
            amount = float(input("How much money would you like to transfer to "))
            if amount <= balance:
                balance -= amount
                print("Transfer completed. Your new balance is ", balance)
            else:
                print("You dont have enough money to transfer")
        else: 
            print("User does not exist.")
    elif choice == "4":
        amount = float(input("How much money would you like to withdraw?: "))
        if amount > balance:
            print("Sorry, you don't have that much money in your account.")
        else:
            balance -= amount
            print("The new available balance is $", balance)        
else:
    print("Incorrect username or password. Please try again.")
    count = 0
    while count < 3:
        user_name = input("Introduce your user name: ")
        password = input("Introduce your password: ")
        if validate_credentials(user_name, password, lists):

            print("You have successfully logged in.")

            balance = 2000
            print("Welcome to your account, ", user_name)
            print("What transactions do you want to do (Introduce the number of your choice): ")
            print("1) View")
            print("2) Deposit")
            print("3) Transfer")
            print("4) Withdraw")
            choice = input()

            if choice == "1":
                print("Your balance is ",balance )
            elif choice == "2":
                amount=float(input("How much money would you like to deposit? "))
                balance +=amount
                print("Your balance now is: ", balance)
            elif choice == "3":
                user = input("Enter the name of the user you want to deposite to: ").capitalize()
                if validate_user(user,users):
                    amount = float(input("How much money would you like to transfer to "))
                    if amount <= balance:
                        balance -= amount
                        print("Transfer completed. Your new balance is ", balance)
                    else:
                        print("You dont have enough money to transfer")
                else: 
                    print("User does not exist.")
            elif choice == "4":
                amount = float(input("How much money would you like to withdraw?: "))
                if amount > balance:
                    print("Sorry, you don't have that much money in your account.")
                else:
                    balance -= amount
                    print("The new available balance is $", balance)        
            break
        else:
            print("Incorrect username or password. Please try again.")
            count += 1
            if count >= 3:
                print("Too many failed attempts. The system will be shut down.")
