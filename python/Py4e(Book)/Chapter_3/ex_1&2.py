try:
    hour = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    pay = 0

    if hour > 40:
        pay = (40 * rate) + ((hour - 40) * (rate * 1.5))
    else:
        pay = hour * rate
    
    print(f"Pay: {pay}")
except:
    print("Please enter a number !")