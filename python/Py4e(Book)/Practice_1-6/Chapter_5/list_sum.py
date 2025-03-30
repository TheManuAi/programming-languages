user_input = input("Enter a number (or 'done' to finish): ")
numbers = []

while user_input != "done":
    try:
        number = int(user_input)
        numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")
    user_input = input("Enter a number (or 'done' to finish): ")

total = 0
for i in numbers:
    total += i

print("The sum of the numbers is:", total)
