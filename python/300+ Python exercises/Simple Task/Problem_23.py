day = input("Enter the day of the week: ").strip().lower()

if day == "sunday":
    print("Happy Holiday !")
else:
    print(f"There is no holiday on {day.capitalize()}")