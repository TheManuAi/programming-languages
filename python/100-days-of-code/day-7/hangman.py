import random
from hangman_words import word_list
from hangman_art import logo, stages

# Print the hangman logo
print(logo)

# Randomly choose a word from the word list
chosen_word = random.choice(word_list)
lives = 6

# Create a placeholder for the word to guess
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

# Main game loop
while not game_over:

    print(f"**************************** {lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # Check if the letter has already been guessed
    if guess in correct_letters:
        print(f"You've already guessed {guess}, try again.")

    display = ""

    # Update the display with correct guesses
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # If the guessed letter is not in the word, lose a life
    if guess not in chosen_word:
        print(f"Sorry, {guess} is not in the word. You lose a life.")
        lives -= 1

        # If no lives are left, the game is over
        if lives == 0:
            game_over = True
            print("The word was: " + chosen_word)
            print(f"***********************YOU LOSE**********************")

    # If there are no more underscores, the player wins
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Print the current stage of the hangman
    print(stages[lives])