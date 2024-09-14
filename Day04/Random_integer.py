import random

# Define two numbers for range-based random number generation.
num1 = 5
num2 = 10

# Generate and print a random integer between num1 and num2 (inclusive).
print(f'Random number between {num1} and {num2}: ', random.randint(num1, num2))

# Generate and print a random float number between 0.0 and 1.0.
print('Random number from 0 to 1: ', random.random())

# Generate and print a random float number with a uniform distribution between 1 and 5.
print('Uniform Distribution between [1,5]:', random.uniform(1, 5))

# Generate and print a random float number from a Gaussian distribution with mean 0 and standard deviation 1.
print('Gaussian Distribution with mean = 0 and standard deviation = 1:', random.gauss(0, 1))

# Generate a random float number between 0 and 5.
random_float = random.random() * 5
print(random_float)

# Generate and print a random integer between 1 and 100 (inclusive) as a "love score".
love_score = random.randint(1, 100)
print(f'Your love score is {love_score}')