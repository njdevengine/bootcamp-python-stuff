# The list of candies to print to the screen
candyList = [
    "Snickers",
    "Kit Kat",
    "Sour Patch Kids",
    "Juicy Fruit",
    "Swedish Fish",
    "Skittles",
    "Hershey Bar",
    "Skittles",
    "Starbursts",
    "M&Ms",
]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candyCart = []
print()

for candy in candyList:
    print("[" + str(candyList.index(candy)) + "]" + candy)

for candies in range(0, allowance):
    userchoice = input("Which candies do you want?")
    print(userchoice)
    candyCart.append(candyList[int(userchoice)])

print(candyCart)
