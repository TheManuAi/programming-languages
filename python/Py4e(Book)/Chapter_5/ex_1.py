count = 0
total = 0
avg = 0

while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        try:
            int(num)
            count += 1
            total += int(num)
            avg = total / count
        except:
            print("Invalid input")
    except:
            continue
    
print(f"Total Number of elements: {count}")
print(f"Sum of all the elements: {total}")
print(f"Average of all the elements: {avg}")