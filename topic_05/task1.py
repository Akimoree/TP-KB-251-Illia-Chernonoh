import random

choices = ["stone", "scissor", "paper"]

user = input("Enter stone, scissor or paper: ").lower()
while user not in choices:
    print("Wrong value")
    user = input("Enter stone, scissor or paper: ").lower()

computer = random.choice(choices)
print("Computer chose:", computer)

if user == computer:
    print("Draw")
elif user == "stone" and computer == "scissor":
    print("You win")
elif user == "scissor" and computer == "paper":
    print("You win")
elif user == "paper" and computer == "stone":
    print("You win")
else:
    print("Computer wins")