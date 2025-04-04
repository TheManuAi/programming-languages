string = input("Enter a text: ").strip().lower()

vowel = 0
consonant = 0
num = 0
for i in string:
    if i.isalpha():
        if i in ("a", "e", "i", "o", "u"):
            vowel += 1
        else:
            consonant += 1
    elif i.isdigit():
        num += 1
print(f"There are {vowel} vowels, {consonant} consonents and {num} numbers.")