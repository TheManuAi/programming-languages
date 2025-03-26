principle_amount = float(input("Enter the principle amount: "))
annual_interest = float(input("Enter the annual interest(in percentage): "))
time = float(input("Enter the time(in years): "))

final_amount = principle_amount * (1 + (annual_interest * 0.01) * time)

interest = final_amount - principle_amount

print(f"Interest is: {interest.__round__(2)}")
print(f"Final amount is: {final_amount.__round__(2)}")