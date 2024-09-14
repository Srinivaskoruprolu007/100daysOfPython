import random
from Hangman_words import word_list  # Importing the list of words for the game
from Hangman_art import logo, stages  # Importing ASCII art for game branding and stages

# Choose a random word from the word list
chose_name = random.choice(word_list)
word_length = len(chose_name)
end_of_game = False  # Flag to determine if the game has ended
lives = 6  # Number of lives the player has

print(logo)  # Print the logo for the game

# Initialize display with underscores representing each letter in the chosen word
display = set("_" for _ in range(word_length))

# Game loop
while not end_of_game:
    # Prompt user for a letter guess and convert to lowercase
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter has already been guessed
    if guess in display:
        print(f"You already guessed the letter '{guess}'.")
    else:
        found = False
        # Check each position in the chosen word
        for position in range(word_length):
            letter = chose_name[position]
            # If the guessed letter matches a letter in the chosen word
            if letter == guess:
                display.add(letter)
                found = True

        # If the letter was not found in the word
        if not found:
            print(f"You guessed '{guess}' a wrong letter. Guess again! You lose a life.")
            lives -= 1
            # Check if the player has run out of lives
            if lives == 0:
                end_of_game = True
                print("You lost.")
                print(f"The word was: {chose_name}")

    # Print the current state of the word with guessed letters and underscores
    print("".join(letter if letter in display else "_" for letter in chose_name))

    # Check if the player has guessed all the letters in the word
    if display == set(chose_name):
        end_of_game = True
        print("You win!")

    # Print the current stage of the hangman
    print(stages[lives])