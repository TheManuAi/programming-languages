try:
    grade = float(input("Enter score: "))
    
    if grade > 100 or grade < 0:
        print("Invalid score")
    elif grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    elif grade >= 50:
        print("E")
    else:
        print("F")
except:
    print("Invalid score")