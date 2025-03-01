def computpay(hour, rate):
    pay = 0
    if hour > 40:
        pay = (40 * rate) + ((hour - 40) * (rate * 1.5))
    else:
        pay = hour * rate
    return pay
        
    
    
try:
    hour = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    print(f"Pay: {computpay(hour, rate)}")
except:
    print("Please enter a number !")