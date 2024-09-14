import random  # To use random for card dealing.
from replit import clear  # Clears the console between rounds.
from Black_Jack_art import logo  # The logo for the game (assumed to be defined elsewhere).

# Function to deal a card randomly
def deal_card():
    """
    Returns a random card from the deck.
    :return: int
    """
    # The deck where cards are represented by numbers (11 represents Ace).
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)  # Randomly chooses a card from the deck.
    return card

# Function to calculate the score of a hand
def calculate_score(cards: list) -> int:
    """
    Takes a list of cards and returns the score calculated from cards.
    
    :param cards: list of integers representing the hand of cards.
    :return: int - calculated score.
    """
    # A Blackjack is represented by a score of 21 with 2 cards (Ace + 10).
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Represents Blackjack (an automatic win).

    # If the hand contains an Ace (11) and the score goes over 21, convert Ace to 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    # Return the total score of the cards.
    return sum(cards)

# Function to compare the user's score with the computer's score and return the result
def compare(user_score: int, computer_score: int) -> str:
    """
    Compares the user's score and computer's score to determine the winner.
    
    :param user_score: int - the player's score.
    :param computer_score: int - the computer's score.
    :return: str - the result of the comparison.
    """
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 🤯"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😑"

# The main game function
def play_game():
    print(logo)  # Print the Blackjack game logo (assuming it's defined in 'Black_Jack_art').

    user_cards = []  # List to store the user's cards.
    computer_cards = []  # List to store the computer's cards.
    is_game_over = False  # Boolean to control the game loop.

    # Deal two initial cards to both the user and the computer.
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Continue the game until the user decides to stop or the game ends.
    while not is_game_over:
        # Calculate the current scores for the user and the computer.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Display the user's cards and the computer's first card.
        print(f"Your cards: {user_cards}, current score = {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for Blackjack or if the user's score is over 21.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask the user if they want another card.
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:  ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())  # Add another card to the user's hand.
            else:
                is_game_over = True

    # Computer's turn: continue drawing cards until score reaches 17 or more.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Display the final hands and scores.
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    # Determine the result by comparing scores.
    print(compare(user_score, computer_score))

# Loop to allow multiple rounds of the game.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    clear()  # Clear the console for a new round.
    play_game()