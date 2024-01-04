"""Create an online banking system with the following features:

* Users must be able to log in with a username and password.
* If the user enters the wrong credentials three times, the system must lock them out.
* The initial balance in the bank account is $2000.
* The system must allow users to deposit, withdraw, view, and transfer money.
* The system must display a menu for users to perform transactions."""


print("Online banking system")

print("Do you have an account already?")
print("To log in enter 's'.")
print("To sign up enter 'n'.")
option = input()
if option == "s":
    user_name = input("Introduce your user name: ")
    password = input("Introduce your password: ")
elif option == "n":
    name = input("Please introduce your name.")
    user = input("Please create an user.")
    mail = input("Please introduce your email.")
    passw = input("Please create a password.")
    print("\nYour data has been registered.\n\nNow you can login.")
else:
    print("The option is incorrect. Try again. ")
lists = []
lists.append(name)
lists.append(user)
lists.append(mail)
lists.append(passw)

val = 0
pos = 0
while val < len(lists)-1:
    user1 = lists[pos]
    if user_name == user1 and password == user1:
        val += 1
        pos = val
    else:
        print("Wrong user or password. You have 3 more attempts left.")


