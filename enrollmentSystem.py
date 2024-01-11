"""
3. Create an university enrollment system with the following characteristics:
* 		The system has a login with a username and password.
* 		Upon logging in, a menu displays the available programs: Computer Science, Medicine, Marketing, and Arts.
* 		The user must input their first name, last name, and chosen program.
* 		Each program has only 5 available slots. The system will store the data of each registered user, and if it exceeds the limit, it should display a message indicating the program is unavailable.
* 		If login information is incorrect three times, the system should be locked.
* 		The user must choose a campus from three cities: London, Manchester, Liverpool.
* 		In London, there is 1 slot per program; in Manchester, there are 3 slots per program, and in Liverpool, there is 1 slot per program.
* 		If the user selects a program at a campus that has no available slots, the system should display the option to enroll in the program at another campus.
"""

def user_signup():
    name = input("Enter your name: ")
    mail = input("Enter your email: ")
    passw = input("Enter your password: ")
    conf_passw = input("Confirm your password: ")
    if passw == conf_passw:
        print("\nYour account was created successfully!")
        data_user = [name,passw]
    else:
        print("The passwords doesn't match. Try again.")
    return data_user

def user_login(user,password,data_user):
    attempts = 0
    while attempts <= 3:
        if user == data_user[0] and password == data_user[1]:
            message = "You have succesfuly log in. "
            break
        else:
            print("Wrong username or password. Try again")
            user = input("Enter your user name: ")
            password = input("Enter your password")
        attempts += 1
        if attempts == 3: 
            message = "Your account was locked due to too many failed attempts."
            break
    return message

def show_menu():
    print("\n--- Available Programs ---\n")
    print("1 - Computer Science")
    print("2 - Medicine")
    print("3 - Marketing")
    print("4 - Arts\n")
    choice = input("Enter the number of your choice: ")
    return int(choice)

def user_information():
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    program = show_menu()
    return program

def cities(city,limit1,limit2,limit3):
    slot_london = limit1
    slot_manchester = limit2
    slot_liverpool = limit3
    if city == 1:
        slot_london += 1
        if slot_london > 1:
            message ="This session is full. Try choosing another city. "
        else:
            message = "You have selected the campus in the city of London. Your enrollment is complete!"
    elif city == 2:
        slot_manchester += 1
        if slot_manchester > 3:
            message = "This session is full. Try choosing another city. "
        else:
            message = "You have selected the campus in the city of Manchester. Your enrollment is complete!"
    elif city == 3:
        slot_liverpool += 1
        if slot_london > 1:
            message = "This session is full. Try choosing another city. "
        else:
            message = "You have selected the campus in the city of Manchester. Your enrollment is complete!"
    return message

def Computer_Science():
    print("You have selected the program of Computer Science. \nThere are only 5 available slots. Choose the campus in the city of your preference ")
    city = int(input("Available cities: 1- London, 2- Manchester, 3- Liverpool"))
    while city < 1 or city > 3:
        print("Invalid Option. Please try again.")
        city = int(input("Available cities: 1- London, 2- Manchester, 3- Liverpool"))
    city_slots = cities(city,1,1,1)
    print(city_slots)
    while city_slots == "This session is full. Try choosing another city. ":
        city2 = int(input("Available cities: 1- London, 2- Manchester, 3- Liverpool"))
        city_slots2 = cities(city2,1,1,1)
        print(city_slots2)
        break
    message = "\nThank you for using The Enrollment System."
    return message 

def Medicine():
    print("You have selected the program of Medicine. \nThere are only 5 available slots. Choose the campus in the city of your preference ")
    city = int(input("Available cities: 1- London, 2- Manchester, 3- Liverpool: "))
    while city < 1 or city > 3:
        print("Invalid Option. Please try again.")
        city = int(input("Available cities: 1- London, 2- Manchester, 3- Liverpool: "))
    city_slots = cities(city,0,3,0)
    print(city_slots)
    while city_slots == "This session is full. Try choosing another city. ":
        city2 = int(input("Available cities: 1- London, 2- Manchester, 3- Liverpool: "))
        city_slots2 = cities(city2,0,3,0)
        print(city_slots2)
        break
    message = "\nThank you for using The Enrollment System."
    return message

def Marketing():
    print("You have selected the program of Marketing. \nThere are only 5 available slots. Choose the campus in the city of your preference ")
    city = int(input("Available cities: 1- London, 2- Manchester, 3- Liverpool: "))
    while city < 1 or city > 3:
        print("Invalid Option. Please try again.")
        city = int(input("Available cities: 1- London, 2- Manchester, 3- Liverpool: "))
    city_slots = cities(city,0,1,1)
    print(city_slots)
    while city_slots == "This session is full. Try choosing another city. ":
        city2 = int(input("Available cities: 1- London, 2- Manchester, 3- Liverpool: "))
        city_slots2 = cities(city2,0,1,1)
        print(city_slots2)
        break
    message = "\nThank you for using The Enrollment System."
    return message

def Arts():
    print("You have selected the program of Arts. \nThere are only 5 available slots. Choose the campus in the city of your preference ")
    city = int(input("Available cities: 1- London, 2- Manchester, 3- Liverpool"))
    while city < 1 or city > 3:
        print("Invalid Option. Please try again.")
        city = int(input("Available cities: 1- London, 2- Manchester, 3- Liverpool"))
    city_slots = cities(city,0,0,0)
    print(city_slots)
    while city_slots == "This session is full. Try choosing another city. ":
        city2 = int(input("Available cities: 1- London, 2- Manchester, 3- Liverpool"))
        city_slots2 = cities(city2,0,0,0)
        print(city_slots2)
        break
    message = "\n Thank you for using The Enrollment System."
    return message 




print("Welcome to the University System Enrollment")
print("\nIf you have an account enter 'Y' otherwise enter 'n': ")
option = input().upper()
if option == 'Y':
    username = input("Enter your Username: ").capitalize()
    password = input("Enter your Password: ").capitalize()
    user1 = ["Nacho","Nachito"]
    login = user_login(username,password,user1)
    if login == "You have succesfuly log in. ":
        menu = show_menu()
        if menu == 1:
            choice = Computer_Science()
            print(choice)
        elif menu == 2:
            choice = Medicine()
            print(choice)
        elif menu == 3:
            choice = Marketing()
            print(choice)
        elif menu == 4:
            choice = Arts()
            print(choice)
elif option =='N':
    user = user_signup()
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    login = user_login(username,password,user)
    if login == "You have succesfuly log in. ":
        menu = show_menu()
        if menu == 1:
            choice = Computer_Science()
            print(choice)
        elif menu == 2:
            choice = Medicine()
            print(choice)
        elif menu == 3:
            choice = Marketing()
            print(choice)
        elif menu == 4:
            choice = Arts()
            print(choice)