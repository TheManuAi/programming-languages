def count(word, letter):
    occurance = 0
    for let in word:
        if let == letter:
            occurance += 1
    print(f"The {letter} comes {occurance} times")
    

word = input("Enter the word: ")
letter = input("Enter the charachter whose occurance you are intrested in: ")

count(word=word, letter=letter)
