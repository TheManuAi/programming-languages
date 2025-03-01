try:
    score = float(input("Enter score (0-100): "))
    if score > 100 or score < 0:
        print("Score is not valid !")
    elif score <= 100 and score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    elif score < 60:
        print("F")
except:
    print("Please enter a numaric value (0-100)")