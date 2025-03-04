import random

random_choice = random.randint(1, 2)

if random_choice == 1:
    coin = "Heads"
else:
    coin = "Tails"

print(f"After the flipping the coin the result is {coin}")