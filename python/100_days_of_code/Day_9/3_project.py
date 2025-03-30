from os import system
from art import logo

print(logo)
print("Welcome to the secret auction program.")

data = {}
while True:
    try:
        name = input("What is your name: ")
        price = float(input("What's your bid: "))
        data[name] = price
        bidders = input("Are there any other bidders (type \"yes\" to continue): ")
        if bidders == "yes":
            system("cls")
            continue
        else:
            break
    except ValueError:
        print("Sorry, I didn't understand that.")
        break

highest = 0
highest_bidder = "No-one"
for key in data:
    if data[key] > highest:
        highest = data[key]
        highest_bidder = key

print(f"The highest bidder is {highest_bidder} with a bid of {highest}.")