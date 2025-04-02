print("For area of a Rectangle")
length = input("Enter the length: ")
width = input("Enter the width: ")

try:
    area = float(length) * float(width)
    print(f"The area is {area}")
except ValueError:
    print("Enter valid dimensions")