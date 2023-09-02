import random
from Hangman_words import word_list
from Hangman_art import logo, stages

chose_name = random.choice(word_list)
word_length = len(chose_name)
end_of_game = False
lives = 6

print(logo)

display = set("_" for _ in range(word_length))

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed the letter '{guess}'.")
    else:
        found = False
        for position in range(word_length):
            letter = chose_name[position]
            if letter == guess:
                display.add(letter)
                found = True

        if not found:
            print(f"You guessed '{guess}' a wrong letter. Guess again! You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lost.")
                print(chose_name)

    print("".join(letter if letter in display else "_" for letter in chose_name))

    if display == set(chose_name):
        end_of_game = True
        print("You win!")

    print(stages[lives])
