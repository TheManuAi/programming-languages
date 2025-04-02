print("For area of a Circle")
radius = input("Enter the Radius: ")

try:
    area = 3.14159 * (float(radius) ** 2)
    print(f"The area is {area}")
except ValueError:
    print("Enter a valid radius")