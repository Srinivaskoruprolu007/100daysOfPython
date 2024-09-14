import random

# Define the ASCII art representations of Rock, Paper, and Scissors.
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Store the game images in a list.
game_images = [rock, paper, scissors]

# Get the user's choice and convert it to an integer.
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Display the user's choice.
print(game_images[user_choice])

# Generate a random choice for the computer.
computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

# Determine the game result based on the user's and computer's choices.
if user_choice >= 3 or user_choice < 0:
    # Handle invalid input.
    print("You typed an invalid number, you lose!")
elif user_choice == 0 and computer_choice == 2:
    # Rock beats Scissors.
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    # Scissors lose to Rock.
    print("You lose")
elif computer_choice > user_choice:
    # Determine the winner based on the choices.
    # Paper beats Rock, Rock beats Scissors, Scissors beats Paper.
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    # If the choices are the same, it's a draw.
    print("It's a draw")