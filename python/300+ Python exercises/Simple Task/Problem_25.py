try:
    marks = float(input("Enter marks: "))
    if marks > 40 and marks < 100:
        print("Pass")
    elif marks < 40 and marks > 0:
        print("Fail")
    else:
        print("Enter valid marks!")
except ValueError:
    print("Enter valid marks!")