import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# First solution
random_friend = random.choice(friends)
print(f"The person who will pay the bill is {random_friend}")

# Second solution
# random_friend = random.randint(0, 4)
# person = "who will pay the bill"
#
# if random_friend == 0:
#     person = "Alice"
# elif random_friend == 1:
#     person = "Bob"
# elif random_friend == 2:
#     person = "Charlie"
# elif random_friend == 3:
#     person = "David"
# else:
#     person = "Emanuel"
#
# print(f"The person who will pay the bill is {person}")

# Third solution
# random_index = random.randint(0, 4)
# print(f"The person who will pay the bill is {friends[random_index]}")