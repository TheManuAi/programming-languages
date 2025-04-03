# Compound assignment operators
num1 = float(input("Enter a number to see some compound assignment operations with 5: "))

total = 0
num1 += 5
print(f"First with += {num1}")
total += num1
num1 -= 5
print(f"After that -= {num1}")
total += num1
num1 *= 5
print(f"After that *= {num1}")
total += num1
num1 /= 5
print(f"After that /= {num1}")
total += num1
num1 %= 5
print(f"After that %= {num1}")
total += num1

print(f"The sum of all the values is {total}")