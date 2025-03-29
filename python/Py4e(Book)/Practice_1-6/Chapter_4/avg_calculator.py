def avg():
    numbers = []
    while True:
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number.")
    avg_value = sum(numbers) / len(numbers)
    print(f"The average of the numbers is: {avg_value}")

avg()