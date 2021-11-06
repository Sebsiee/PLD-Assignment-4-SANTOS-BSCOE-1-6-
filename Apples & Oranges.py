def introduction():
    print("Welcome to the Fruit Market!")
    print("The prices of the fruits are:")
    print("Apple=20, Orange=25")

def applesOranges(getApples, getOranges):
    priceApples = 20 * getApples
    priceOranges = 25 * getOranges
    return priceApples + priceOranges

def display():
    getApples = int(input("How many apples do you want to buy? "))
    getOranges = int(input("How many oranges do you want to buy? "))
    totalAmountF = applesOranges(getApples, getOranges)
    print (f"The total amount is {totalAmountF}.")

introduction()
display()
