password = input("Enter the password: ").strip()


if password.isalnum():
    print(f"Your password {len(password) * "*"} is fine")
else:
    print("Sorry we did not allow spaces in between and special character")