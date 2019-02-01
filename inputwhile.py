#create a while loop
cont_play ="y"
#starting number
start_number = 0
#lets start
while cont_play == "y":
    user_number = input("How many numbers?")
    for i in range(int(user_number)):
        print(i)
    cont_play = input("Now do you want to play again? y/n")
