print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
        print("Child tickets are 5$")
    elif 12 == age <= 18:
        bill = 7
        print("Youth tickets are 7$")
    elif 45 <= age <= 55:
        bill = 0
        print("Your tickets are free")
    else:
        bill = 12
        print("Adult tickets are 12$")

    photo = input("Do you have any photo? Type y for Yes and n for No: ")
    if photo == "y" or photo == "Y":
        bill += 3

    print("Your final bill is", bill)
else:
    print("Sorry you have to grow taller before you can ride.")
