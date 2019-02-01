import random
# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection prompt
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if user_choice == computer_choice:
    print('Its a tie')
elif user_choice == "r" and computer_choice == "p":
    print('You Lose')
elif user_choice == "r" and computer_choice == "s":
    print('You Win')
elif user_choice == "p" and computer_choice == "r":
    print('You Win')
elif user_choice == "p" and computer_choice == "s":
    print('You Lose')
elif user_choice == "s" and computer_choice == "r":
    print('You Lose')
elif user_choice == "s" and computer_choice == "p":
    print('You Win')
else:
    print('pick r, p, or s')
