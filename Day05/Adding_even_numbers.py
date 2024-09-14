print("Adding even numbers from 1 to 100")

# Initialize the total sum to 0.
total = 0

# Iterate over the range of even numbers from 2 to 100 (inclusive).
# The range function is set with a step of 2 to ensure only even numbers are considered.
for number in range(2, 101, 2):
    # Add the current even number to the total sum.
    total += number

# Print the final total sum of even numbers.
print(total)