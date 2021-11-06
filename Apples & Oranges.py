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
    solution = str(input("Do you want to see the solution? Y or N "))
    if solution == "Y":
        print(f"20 x {getApples} + 25 x {getOranges} = {totalAmountF}")
    elif solution == "N":
        print("Wow! You already know how it got solved.")
    else:
        print("Input not recognized.")


introduction()
display()

