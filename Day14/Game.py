from Data import data
import random
from art import logo, vs
from replit import clear

def get_random_account():
    """
    Selects and returns a random account from the data list.
    :return: dict representing a random account
    """
    return random.choice(data)

def format_data(account):
    """
    Formats the account data into a human-readable string.
    :param account: dict containing account details
    :return: str in the format "name, a description, from country"
    """
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """
    Checks if the user's guess about who has more followers is correct.
    :param guess: str, user's guess ('a' or 'b')
    :param a_followers: int, follower count for account A
    :param b_followers: int, follower count for account B
    :return: bool, True if the guess is correct, False otherwise
    """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    """
    Runs the game loop, displaying account comparisons and checking user guesses.
    """
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        # Ensure that the new account is different from the previous one
        while account_a == account_b:
            account_b = get_random_account()

        # Display the two accounts for comparison
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        # Get user's guess and check if it's correct
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        # Clear the screen and display the logo
        clear()
        print(logo)
        
        # Update score or end the game based on the user's guess
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

# Start the game
game()
