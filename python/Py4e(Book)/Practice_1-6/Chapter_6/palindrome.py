def palindrome(n):
    formated = n.strip().lower()
    reverse = formated[::-1]
    if formated == reverse:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")


user_input = input("Enter a string to check palindrome: ")
palindrome(user_input)
