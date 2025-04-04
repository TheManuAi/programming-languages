try:
    name = input("Enter the name: ").strip().lower()
    if name == "xyz" and len(name) < 3:
        print("You can't take admission")
    else:
        print("You can take admission!")
except ValueError:
    print("Enter a valid name!")