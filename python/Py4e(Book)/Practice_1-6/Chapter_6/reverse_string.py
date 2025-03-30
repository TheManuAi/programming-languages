user_input = input("Enter a string to reverse: ")
for char in reversed(user_input):
    print(char, end="")

"""
#v2
user_input = input("Enter a string to reverse: ")
print(f"The reversed string is: {user_input[::-1]}")
"""