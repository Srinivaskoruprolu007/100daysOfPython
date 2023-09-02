import random


def play_game():
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    guess = random.randint(1, 100)
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = 10 if choice == 'easy' else 5
    end_game = False

    while attempts > 0 and not end_game:
        print(f"You have {attempts} {'attempt' if attempts == 1 else 'attempts'} to guess the number")

        try:
            user_guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_guess > guess:
            print("Too high")
        elif user_guess < guess:
            print("Too low")
        else:
            print(f"You got it! The answer was {user_guess}")
            end_game = True

        attempts -= 1

    if not end_game:
        print("You have run out of attempts. You lose!")


play_game()
