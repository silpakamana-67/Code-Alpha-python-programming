import random

# List of predefined words
words = ["python", "computer", "developer", "programming", "keyboard"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
max_wrong_guesses = 6
wrong_guesses = 0

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the word one letter at a time!")
print("You have", max_wrong_guesses, "wrong guesses allowed.")

# Main game loop
while wrong_guesses < max_wrong_guesses:

    # Display the word with underscores
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the player has guessed the complete word
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations!")
        print("You guessed the word:", word)
        break

    # Get user's guess
    guess = input("Enter a letter: ").lower()

    # Check whether input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add letter to guessed list
    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

# Game over
else:
    print("\nGame Over!")
    print("The correct word was:", word)

print("\nThanks for playing!")