def introduction():
    print("Welcome!")

def totalApples(moneyAmount, applePrice):
    divApples = moneyAmount / applePrice
    return "%.0f" % divApples 

def totalChange(moneyAmount, applePrice):
    minApples = moneyAmount - applePrice
    return minApples

def display():
    moneyAmount = int(input("Enter the amount of your money: "))
    applePrice = int(input("What is the price of an apple? "))
    firstAppleF = totalApples(moneyAmount, applePrice)
    secondChangeF = totalChange(moneyAmount, applePrice)
    print(f"You can buy {firstAppleF} apples and your change is {secondChangeF} pesos.") 


introduction()
display()