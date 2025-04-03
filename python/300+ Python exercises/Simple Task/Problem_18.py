name = input("Enter your name: ")
age = input("Enter your age: ")
contact = input("Enter your contact number: ")

Dict = {"name": name, "age": age, "contact": contact}

print(f"Your info here is {Dict}")

contact2 = input("Update your contact number: ")

Dict["contact"] = contact2

print(f"Now your info is {Dict}")