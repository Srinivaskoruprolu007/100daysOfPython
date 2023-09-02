import random
num1 = 5
num2 = 10
print(f'Random number between {num1} and {num2} : ', random.randint(num1, num2))
print('Random number from 0 to 1: ', random.random())
print('Uniform Distribution between [1,5] :', random.uniform(1, 5))
print('Gaussian Distribution with mean = 0 and standard deviation = 1 : ', random.gauss(0, 1))

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f'Your love score is {love_score} ')
