count = 0
total = 0
avg = 0
maxm = -100000
minm = 100000000

while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        try:
            int(num)
            count += 1
            total += int(num)
            # avg = total / count
            if int(num) >= -10000 and int(num) > maxm:
                 maxm = int(num)
            if int(num) >= -10000 and int(num) < minm:
                 minm = int(num)
        except:
            print("Invalid input")
    except:
            continue
    
print(f"Total Number of elements: {count}")
print(f"Sum of all the elements: {total}")
print(f"The maximum value is: {maxm}")
print(f"The minimum value is: {minm}")
# print(f"Average of all the elements: {avg}")