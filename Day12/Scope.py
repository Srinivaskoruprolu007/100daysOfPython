############################# Scope ###########################


enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()

print(f"enemies outside function: {enemies}")

# local scope


def drink_portion():
    portion_strength = 2
    print(portion_strength)


drink_portion()
