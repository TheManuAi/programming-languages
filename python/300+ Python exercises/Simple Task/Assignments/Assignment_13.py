password = input("Enter the password: ").strip()


if password.isalnum() and len(password) < 8:
    print(f"Your password {len(password) * "*"} is fine")
else:
    print("Sorry we did not allow spaces in between, special character and length more than or equal to 8")