import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# printing user input
user_choice = input("What do you choose? Type 1 for Rock, 2 for Paper, 3 for Scissors:  ")
if user_choice == "1":
    print("You chose:", rock)
    user_choice = rock
elif user_choice == "2":
    print("You chose:", paper)
    user_choice = paper
elif user_choice == "3":
    print("You chose:", scissors)
    user_choice = scissors
else:
    print("Choose a valid option.")


# printing computer input
computer_chose = random.choice([rock, paper, scissors])
if computer_chose == "1":
    print("Computer chose:", rock)
    computer_chose = rock
elif computer_chose == "2":
    print("Computer chose:", paper)
    computer_chose = paper
else:
    print("Computer chose:", scissors)
    computer_chose = scissors


#logic to decide who won
if user_choice == computer_chose:
    print("It's a Draw!")
elif user_choice == rock and computer_chose == paper:
    print("Computer Won!")
elif user_choice == rock and computer_chose == scissors:
    print("You Won!")
elif user_choice == paper and computer_chose == scissors:
    print("Computer Won!")
elif user_choice == paper and computer_chose == rock:
    print("You Won!")
elif user_choice == scissors and computer_chose == rock:
    print("Computer Won!")
elif user_choice == scissors and computer_chose == paper:
    print("You Won!")

# This logic also works if instead of rock, paper, scissors I used 1 2 and 3 respectively
# if computer_chose > user_choice:
#     print("Computer Won!")
# if computer_chose < user_choice:
#     print("You Won!")
# else:
#     print("It's a Draw!")
