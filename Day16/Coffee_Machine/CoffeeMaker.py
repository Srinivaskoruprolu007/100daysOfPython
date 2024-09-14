class CoffeeMaker:
    """Models the machine that makes the coffee"""

    def __init__(self):
        """
        Initializes the CoffeeMaker with default resources.
        Resources include water, milk, and coffee.
        """
        self.resources = {
            "water": 300,  # in milliliters
            "milk": 200,   # in milliliters
            "coffee": 100  # in grams
        }

    def report(self):
        """
        Prints a report of the current resources in the CoffeeMaker.
        Displays the amount of water, milk, and coffee available.
        """
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """
        Checks if there are enough resources to make the given drink.
        :param drink: An instance of a Drink class with `ingredients` attribute
        :return: True if resources are sufficient, False otherwise
        """
        can_make = True
        # Iterate through each ingredient needed for the drink
        for item in drink.ingredients:
            # Check if there is enough of each ingredient
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """
        Deducts the required ingredients from the CoffeeMaker's resources.
        :param order: An instance of a Drink class with `ingredients` attribute
        """
        # Deduct the ingredients for the drink from the resources
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕. Enjoy!")

# Example usage:

class Drink:
    """Models a coffee drink"""

    def __init__(self, name, ingredients):
        """
        Initializes the Drink with a name and ingredients.
        :param name: Name of the drink
        :param ingredients: Dictionary of ingredients needed for the drink
        """
        self.name = name
        self.ingredients = ingredients

# Creating instances of drinks
espresso = Drink("Espresso", {"water": 50, "coffee": 18})
latte = Drink("Latte", {"water": 200, "milk": 150, "coffee": 24})

# Creating an instance of CoffeeMaker
coffee_maker = CoffeeMaker()

# Printing initial resources
coffee_maker.report()

# Checking if resources are sufficient for espresso
if coffee_maker.is_resource_sufficient(espresso):
    coffee_maker.make_coffee(espresso)
else:
    print("Not enough resources to make espresso.")

# Checking if resources are sufficient for latte
if coffee_maker.is_resource_sufficient(latte):
    coffee_maker.make_coffee(latte)
else:
    print("Not enough resources to make latte.")

# Printing resources after making drinks
coffee_maker.report()
