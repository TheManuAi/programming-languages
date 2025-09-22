import random
#TODO import time and and sleep function so the program looks like it is thinking 

number = random.randint(1,10)
guess = int(input("Guess the random number (hint: it is between 1 to 10): "))
guess_count = 1

while guess != number:
    #TODO add the feature or showing the user they should guess higher or lower and erase the hint after the first input statment 
    guess = int(input("Guess the random number (hint: it is between 1 to 10): "))
    guess_count += 1

print(f"Congrets! You got the right answer which is {number} and it took you {guess_count} tries")
