try:
    number = int(input("Enter a number (enter a nagative number to show the sum): "))
    total = 0
    while number > 0:
        total += number
        number = int(input("Enter a number (enter a nagative number to show the sum): "))
    print(f"The sum of the numbers is {total}")
        
except:
    print("Enter a number!")
    print(f"The sum of the numbers is {total}")
