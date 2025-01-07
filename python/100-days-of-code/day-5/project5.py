import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

# Easy version, where the characters of the password are in order
for i in range(nr_letters):
    password += random.choice(letters)
for i in range(nr_symbols):
    password += random.choice(symbols)
for i in range(nr_numbers):
    password += random.choice(numbers)
#print(password)

# Hard version
# first convert the old(above password) string into a list
# then shuffle it with the help of random module
# and lastly add all the elements of the list back to the string called shuffled_password
password_list = list(password)
random.shuffle(password_list)

shuffled_password = ""
for char in password_list:
    shuffled_password += char

print(f"Your Password should be {shuffled_password}")