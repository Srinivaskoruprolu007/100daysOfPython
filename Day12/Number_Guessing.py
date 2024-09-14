import random


def play_game():
    """
    This is the main function to play the 'Guess the Number' game.

    The game generates a random number between 1 and 100, and the player
    has to guess the number within a limited number of attempts. The difficulty
    level determines the number of attempts. The game gives feedback after each guess, 
    indicating if the guess was too high, too low, or correct.

    Game flow:
    - The player is welcomed and asked to select a difficulty level (easy or hard).
    - The game assigns 10 attempts for easy mode and 5 attempts for hard mode.
    - The game checks each guess and gives feedback.
    - The game ends when the player guesses the correct number or runs out of attempts.
    """

    # Welcome message and random number generation
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    guess = random.randint(1, 100)

    # Asking the user to select a difficulty level
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    # Assigning attempts based on difficulty selection
    attempts = 10 if choice == 'easy' else 5

    # Variable to track whether the game should end
    end_game = False

    # Main game loop
    while attempts > 0 and not end_game:
        # Display remaining attempts
        print(f"You have {attempts} {'attempt' if attempts == 1 else 'attempts'} to guess the number")

        # Input validation: Checking if the user input is a valid number
        try:
            user_guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Giving feedback on the player's guess
        if user_guess > guess:
            print("Too high")
        elif user_guess < guess:
            print("Too low")
        else:
            # If the guess is correct, the game ends
            print(f"You got it! The answer was {user_guess}")
            end_game = True

        # Decrease the number of attempts after each guess
        attempts -= 1

    # If the player runs out of attempts and the game hasn't ended
    if not end_game:
        print(f"You have run out of attempts. You lose! The correct number was {guess}")


# Starting the game
play_game()