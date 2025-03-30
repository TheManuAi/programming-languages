user_input = input("Enter a string: ")
count = 0

for i in user_input:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        count += 1

print(f"The total number of vowel is: {count}")
