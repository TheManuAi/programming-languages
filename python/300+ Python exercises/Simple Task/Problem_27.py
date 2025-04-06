try:
    year = int(input("Enter a year: "))
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        print(f"The {year} is not a leap year")
    else:
        print(f"The {year} is a leap year")
except ValueError:
    print("Enter a valid year")