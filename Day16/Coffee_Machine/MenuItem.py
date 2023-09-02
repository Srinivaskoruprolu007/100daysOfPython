class MenuItem:
    """Models each Menu item"""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the menu with drinks"""
    def __init__(self):
        self.menu = [
            MenuItem("latte", 200, 150, coffee=24, cost=2.5),
            MenuItem("espresso", 50, 0, coffee=18, cost=1.5),
            MenuItem("cappuccino", 250, 50, 24, 3)
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu of the available menu items"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
