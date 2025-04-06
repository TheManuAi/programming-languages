import array as arr

ar = arr.array("i", [])

try:
    for i in range(1, 6):
        ar.append(int(input(f"Enter the {i} year: ")))
except ValueError:
    print("Enter a valid year")

leap_year = []
for a in ar:
    if a % 4 != 0 or (a % 100 == 0 and a % 400 != 0):
        continue
    else:
        leap_year.append(a)

print(f"The leap years are: {leap_year}")