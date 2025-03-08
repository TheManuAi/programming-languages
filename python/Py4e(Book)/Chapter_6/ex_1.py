word = input("Enter a string: ")
print("The reverse is : ")
index = (len(word) - 1) #6
while index >= 0:
    print(word[index])
    index -= 1