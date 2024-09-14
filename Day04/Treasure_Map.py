# Define the rows of the treasure map using emoji squares.
row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

# Combine rows into a 2D list (the full treasure map).
treasure_map = [row1, row2, row3]

# Print the initial state of the treasure map.
print(f"{row1}\n{row2}\n{row3}")

# Prompt the user for the position to place the treasure.
position = input("Where do you want to put the treasure? (Enter the position as two digits, e.g., '23')\n")

# Extract vertical and horizontal coordinates from the input.
vertical = int(position[0])
horizontal = int(position[1])

# Place the treasure (denoted by 'X') at the specified position.
treasure_map[vertical-1][horizontal-1] = "X"

# Print the updated state of the treasure map.
print(f"{row1}\n{row2}\n{row3}")