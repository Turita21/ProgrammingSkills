def menu():
    print("Currency converter")
    print("CLP(Chilean Peso), \nARS(Argentine Peso), \nUSD(Dolares Americanos), \nEUR(Euros),TRY(Lira), \nGBP(Pound Sterling)")


print(menu())

initial_currency = input("Enter yout initial currency (ARS, EUR, USD...): ").upper()
final_currency = input("Enter the currency you want to convert to (CLP, ARS..)").upper()
amount = float(input("How much money do you want to convert: "))


def currency(initial_currency, final_currency,amount):
    if initial_currency == "CLP" and final_currency == "ARS":
        minimun = 500
        if amount > minimun:
            conversion_rate = amount * 0.91
        else: 
            print("The amount of money has to be greater than " + str(minimun) + " CLP. Try again")
    elif initial_currency == "ARS" and final_currency == "CLP":
        minimun = 500
        if amount > minimun:
            conversion_rate = amount * 1.10
        else: 
            print("The amount of money has to be greater than " + str(minimun) + " ARS. Try again")
    elif initial_currency == "CLP" and final_currency == "USD":
        minimun = 10000
        if amount> minimun:
            conversion_rate = amount * 0.0011
        else:
            print("The amount of money has to be greater than " + str(minimun) + " CLP. Try again")
    elif initial_currency == "USD" and final_currency == "CLP":
        minimun = 10
        if amount > minimun:
            conversion_rate = amount * 888.94
        else: 
            print("The amount of money has to be greater than " + str(minimun) + " USD. Try again")
    elif initial_currency == "CLP" and final_currency == "EUR":
        minimun = 10000
        if amount > minimun:
            conversion_rate = amount * 0.0010
        else:
            print("The amount of money has to be greater than " + str(minimun) + " CLP. Try again")
    elif initial_currency == "EUR" and final_currency == "CLP":
        minimun = 10
        if amount > minimun:
            conversion_rate = amount * 973.81
        else:
            print("The amount of money has to be greater than " + str(minimun) + " EUR. Try again")
    elif initial_currency == "CLP" and final_currency == "TRY":
        minimun = 10000
        if amount > minimun:
            conversion_rate = amount * 0.033
        else:
            print("The amount of money has to be greater than " + str(minimun) + " CLP. Try again")
    elif initial_currency == "CLP" and final_currency == "GBP":
        minimun = 10000
        if amount > minimun:
            conversion_rate = amount * 0.00088
        else:
            print("The amount of money has to be greater than " + str(minimun) + " CLP. Try again")
    elif initial_currency == "ARS" and final_currency == "USD":
        minimun = 10000
        if amount > minimun:
            conversion_rate = amount * 0.0012
        else:
            print("The amount of money has to be greater than " + str(minimun) + " ARS. Try again")
    elif initial_currency == "ARS" and final_currency == "EUR":
        minimun = 10000
        if amount > minimun:
            conversion_rate = amount * 0.0011
        else:
            print("The amount of money has to be greater than " + str(minimun) + " ARS. Try again")
    elif initial_currency == "ARS" and final_currency == "TRY":
        minimun = 10000
        if amount > minimun:
            conversion_rate = amount * 0.037
        else:
            print("The amount of money has to be greater than " + str(minimun) + " ARS. Try again")
    elif initial_currency == "ARS" and final_currency == "GBP":
        minimun = 10000
        if amount > minimun:
            conversion_rate = amount * 0.00097
        else:
            print("The amount of money has to be greater than " + str(minimun) + " ARS. Try again")
    elif initial_currency == "USD" and final_currency == "ARS":
        minimun = 10
        if amount > minimun:
            conversion_rate = amount * 811.20
        else:
            print("The amount of money has to be greater than " + str(minimun) + " USD. Try again")
    elif initial_currency == "USD" and final_currency == "EUR":
        minimun = 10
        if amount > minimun:
            conversion_rate = amount * 0.91
        else:
            print("The amount of money has to be greater than " + str(minimun) + " USD. Try again")
    elif initial_currency == "USD" and final_currency == "TRY":
        minimun = 10
        if amount > minimun:
            conversion_rate = amount * 29.82
        else:
            print("The amount of money has to be greater than " + str(minimun) + " USD. Try again")
    elif initial_currency == "USD" and final_currency == "GBP":
        minimun = 10
        if amount > minimun:
            conversion_rate = amount * 0.79
        else:
            print("The amount of money has to be greater than " + str(minimun) + " USD. Try again")
    elif initial_currency == "EUR" and final_currency == "ARS":
        minimun = 10
        if amount > minimun:
            conversion_rate = amount * 888.87
        else:
            print("The amount of money has to be greater than " + str(minimun) + " EUR. Try again")
    elif initial_currency == "EUR" and final_currency == "USD":
        minimun = 5
        if amount > minimun:
            conversion_rate = amount * 1.10
        else:
            print("The amount of money has to be greater than " + str(minimun) + " EUR. Try again")
    elif initial_currency == "EUR" and final_currency == "TRY":
        minimun = 5
        if amount > minimun:
            conversion_rate = amount * 32.68
        else:
            print("The amount of money has to be greater than " + str(minimun) + " EUR. Try again")
    elif initial_currency == "EUR" and final_currency == "GBP":
        minimun = 11
        if amount > minimun:
            conversion_rate = amount * 0.86
        else:
            print("The amount of money has to be greater than " + str(minimun) + " EUR. Try again")
    elif initial_currency == "TRY" and final_currency == "CLP":
        minimun = 5
        if amount > minimun:
            conversion_rate = amount * 29.81
        else:
            print("The amount of money has to be greater than " + str(minimun) + " EUR. Try again")
    elif initial_currency == "TRY" and final_currency == "ARS":
        minimun = 5
        if amount > minimun:
            conversion_rate = amount * 27.20
        else:
            print("The amount of money has to be greater than " + str(minimun) + " EUR. Try again")
    elif initial_currency == "TRY" and final_currency == "USD":
        minimun = 800
        if amount > minimun:
            conversion_rate = amount * 0.034
        else:
            print("The amount of money has to be greater than " + str(minimun) + " EUR. Try again")
    elif initial_currency == "TRY" and final_currency == "EUR":
        minimun = 800
        if amount > minimun:
            conversion_rate = amount * 0.031
        else:
            print("The amount of money has to be greater than " + str(minimun) + " EUR. Try again")
    elif initial_currency == "TRY" and final_currency == "GBP":
        minimun = 900
        if amount > minimun:
            conversion_rate = amount * 0.026
        else:
            print("The amount of money has to be greater than " + str(minimun) + " EUR. Try again")
    elif initial_currency == "GBP" and final_currency == "CLP":
        minimun = 5
        if amount > minimun:
            conversion_rate = amount * 1132.46
        else:
            print("The amount of money has to be greater than " + str(minimun) + " EUR. Try again")
    elif initial_currency == "GBP" and final_currency == "ARS":
        minimun = 5
        if amount > minimun:
            conversion_rate = amount * 1032.25
        else:
            print("The amount of money has to be greater than " + str(minimun) + " EUR. Try again")
    elif initial_currency == "GBP" and final_currency == "USD":
        minimun = 5
        if amount > minimun:
            conversion_rate = amount * 1.27
        else:
            print("The amount of money has to be greater than " + str(minimun) + " EUR. Try again")
    elif initial_currency == "GBP" and final_currency == "EUR":
        minimun = 5
        if amount > minimun:
            conversion_rate = amount * 1.16
        else:
            print("The amount of money has to be greater than " + str(minimun) + " EUR. Try again")
    elif initial_currency == "GBP" and final_currency == "TRY":
        minimun = 5
        if amount > minimun:
            conversion_rate = amount * 37.95
        else:
            print("The amount of money has to be greater than " + str(minimun) + " EUR. Try again")
        conversion_rate = initial_currency * 37.95
    return conversion_rate

whitdraw = input("Do you want to withdraw your founds (Y/n): ").upper()
if whitdraw == "Y":
    change = currency(initial_currency,final_currency,amount)
    commission = 1/100 * change
    total = change - commission
    print("Your total including the comission of withdraw is: " + str(total))
    option = input("Do you want to perform another operation? (Y/n): ").upper()
    if option == "Y":
        print(menu())
        initial_currency = input("Enter yout initial currency (ARS, EUR, USD...): ").upper()
        final_currency = input("Enter the currency you want to convert to (CLP, ARS..)").upper()
        amount = float(input("How much money do you want to convert: "))
        whitdraw = input("Do you want to withdraw your founds (Y/n): ").upper()
        if whitdraw == "Y":
            change = currency(initial_currency,final_currency,amount)
            commission = 1/100 * change
            total = change - commission
            print("Your total including the comission of withdraw is: " + str(total))
        elif whitdraw == "N":
            change = currency(initial_currency,final_currency,amount)
            print(f"The conversion of the currency {initial_currency} to {final_currency} is {change} {final_currency}")
            print("Thank you for use the Currency Converter.")
    else:
        print("Thank you for use the Currency Converter.")
elif whitdraw == "N":
    change = currency(initial_currency,final_currency,amount)
    print(f"The conversion of the currency {initial_currency} to {final_currency} is {change} {final_currency}")
else:
    print("Your choice is no correct. ")
