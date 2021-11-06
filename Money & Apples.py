def introduction():
    print("Welcome!")

def totalApples(moneyAmount, applePrice):
    divApples = moneyAmount // applePrice
    return divApples 

def totalChange(moneyAmount, applePrice):
    minApples = moneyAmount % applePrice
    return minApples

def display():
    moneyAmount = int(input("Enter the amount of your money: "))
    applePrice = int(input("What is the price of an apple? "))
    firstAppleF = totalApples(moneyAmount, applePrice)
    secondChangeF = totalChange(moneyAmount, applePrice)
    if int(firstAppleF) > 1:
        print(f"You can buy {firstAppleF} apples and your change is {secondChangeF} pesos.") 
    elif int(firstAppleF) == 1:
        print(f"You can buy {firstAppleF} apple and your change is {secondChangeF} pesos.")
    else:
        print("You can't buy an apple.") 
        borrowMoney = str(input("Do you want to borrow some money? Y or N: "))
        if borrowMoney == "Y":
            while True:
                try:
                    borrowed = int(input("How much money do you want to borrow? "))
                    borrowedApple = borrowed + moneyAmount
                    solutionBorrowed = borrowedApple // applePrice
                except ValueError:
                    print("Sorry, I didn't understand that.")
                    continue

                if int(borrowedApple) < applePrice:
                    print("You need to borrow more money to buy apples.")
                    continue
                else:
                    break      
            if int(solutionBorrowed) > 1:
             print(f"You bought {solutionBorrowed} apples by borrowing money.")
            elif int(solutionBorrowed) == 1:
                print (f"You bought {solutionBorrowed} apple by borrowing money.")

        elif borrowMoney == "N":
            print("You don't want like apples then.")
        else:
            print("Sorry, I didn't understand that.")



introduction()
display()