"""5. Develop a finance management application with the following features:
* 		The user records their total income.
* 		There are categories: Medical expenses, household expenses, leisure, savings, and education.
* 		The user can list their expenses within the categories and get the total for each category.
* 		The user can obtain the total of their expenses.
* 		If the user spends the same amount of money they earn, the system should display a message advising the user to reduce expenses in the category where they have spent the most money.
* 		If the user spends less than they earn, the system displays a congratulatory message on the screen.
* 		If the user spends more than they earn, the system will display advice to improve the user's financial health.
"""
print("\n Welcome to the Finance Managment Application \n")
print("-----------------------------------------------------")
name  = input("Enter your name: ")
income = float(input("Enter your monthly income: "))

print("If you enter a 0, it indicates that you have finished entering the data for each category, therefore, the system moves to the next category.")

def medical_expenses():
    bill = float(input("Enter your medical expenses: "))
    total_bill = bill
    while bill != 0:
        bill = float(input("Enter your medical expenses: "))
        total_bill += bill
    return total_bill

def household_expenses():
    bill = float(input("Enter your household expenses: "))
    total_bill = bill
    while bill != 0:
        bill = float(input("Enter your household expenses: "))
        total_bill += bill
    return total_bill

def leisure_expenses():
    bill = float(input("Enter your leisure expenses: "))
    total_bill = bill
    while bill != 0:
        bill = float(input("Enter your leisure expenses: "))
        total_bill += bill
    return total_bill

def savings_expenses():
    bill = float(input("Enter your saivings expenses: "))
    total_bill = bill
    while bill != 0:
        bill = float(input("Enter your saivings expenses: "))
        total_bill += bill
    return total_bill

def education_expenses():
    bill = float(input("Enter your education expenses: "))
    total_bill = bill
    while bill != 0:
        bill = float(input("Enter your education expenses: "))
        total_bill += bill
    return total_bill

medical_expenses = medical_expenses()
household_expenses = household_expenses()
leisure_expenses = leisure_expenses()
savings_expenses = savings_expenses()
education_expenses = education_expenses()

print("Medical Expenses", "Household Expenses","Leisure", "Savings", "Education")
list_total = [medical_expenses, household_expenses, leisure_expenses, savings_expenses, education_expenses] 
print(list_total)

sum_total = list_total[0] + list_total[1] + list_total[2] + list_total[3] + list_total[4]
print("Your have spent a total of: " + str(sum_total))

if income == sum_total:
    mayor_expensive = 0
    for i in list_total:
        if i > mayor_expensive:
            mayor_expensive = i
            if mayor_expensive == list_total[0]:
                print("Your most expensive bill was in the Medical Expenses and is a total of: " + str(mayor_expensive))
            elif mayor_expensive == list_total[1]:
                print("Your most expensive bill was in the Household Expenses and is a total of: " + str(mayor_expensive))
            elif mayor_expensive == list_total[2]:
                print("Your most expensive bill was in the Leisure Expenses and is a total of: " + str(mayor_expensive))
            elif mayor_expensive == list_total[3]:
                print("Your most expensive bill was in the Savings Expenses and is a total of: " + str(mayor_expensive))
            elif mayor_expensive == list_total[4]:
                print("Your most expensive bill was in the Education Expenses and is a total of: " + str(mayor_expensive))
elif income > sum_total:
    print("Congratulations!!! You have earn more than you spent!! ")
else:
    print("Carefull! You need to check your finances")