try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"Hi {name.capitalize().strip()}!, Your age is {age}")
except ValueError:
    print("Enter a valid input")