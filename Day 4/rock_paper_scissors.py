from random import randint
from sys import exit

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

sign_mapping = {
    0: rock,
    1: paper,
    2: scissors
}

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for " +
                    "Scissors.\n"))
if not user_input in sign_mapping:
    print("Invalid Input")
    exit()
print(sign_mapping[user_input])

print("Computer chose:")
computer_input = randint(0,2)
print(sign_mapping[computer_input])

if user_input == computer_input:
    print("Draw!")
else:
    if user_input == 0:
        if computer_input == 1:
            print("You Lose!")
        else:
            print("You Win!")
    if user_input == 1:
        if computer_input == 2:
            print("You Lose!")
        else:
            print("You Win!")
    if user_input == 2:
        if computer_input == 0:
            print("You Lose!")
        else:
            print("You Win!")
