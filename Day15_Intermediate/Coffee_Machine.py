from Coffee_Machine_Data import resources, profit, MENU

def is_resources_sufficient(order_ingredients):
    """
    Checks if there are enough resources to make the requested drink.
    
    :param order_ingredients: dict, ingredients required for the drink
    :return: bool, True if resources are sufficient, False otherwise
    """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True

def isTransaction_Successful(money_received, drink_cost):
    """
    Checks if the payment is sufficient for the requested drink.
    
    :param money_received: float, amount of money inserted
    :param drink_cost: float, cost of the drink
    :return: bool, True if the transaction is successful, False otherwise
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is the ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """
    Deducts the required ingredients from the resources and prepares the coffee.
    
    :param drink_name: str, name of the drink to be made
    :param order_ingredients: dict, ingredients required for the drink
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} ☕')

def process_coins():
    """
    Calculates the total amount of money inserted by the user.
    
    :return: float, total amount of money inserted
    """
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def Coffee_Machine():
    """
    Main function to run the coffee machine program. It handles user input,
    processes orders, and interacts with the other functions to serve coffee.
    """
    is_on = True

    while is_on:
        choice = input("What would you like ? (espresso/ latte/ cappuccino) : ").lower()
        if choice == "off":
            is_on = False

        elif choice == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}gm")
            print(f"Money: ${profit}")
        else:
            drink = MENU[choice]
            if is_resources_sufficient(drink['ingredients']):
                payment = process_coins()
                if isTransaction_Successful(payment, drink['cost']):
                    make_coffee(choice, drink['ingredients'])

# Start the coffee machine
Coffee_Machine()
