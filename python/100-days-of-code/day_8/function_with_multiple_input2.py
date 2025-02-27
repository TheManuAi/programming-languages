def greet(name, location):
    print(f"Hello, {name}!")
    print(f"How's the weather at {location}?")

n = input("What is your name: ")
l = input("Where are you live: ")
greet(name = n, location = l)