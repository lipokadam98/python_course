MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,
}


class Ingredients:
    water: int
    milk: int
    coffee: int
    cost: float

    def __init__(self, water, milk, coffee, cost):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.cost = cost


def print_report():
    print(f'Water: {get_remaining_water()}ml')
    print(f'Milk: {get_remaining_milk()}ml')
    print(f'Coffe: {get_remaining_coffee()}g')
    print(f'Money: ${get_remaining_money()}')


def get_remaining_water():
    return resources["water"]


def get_remaining_milk():
    return resources["milk"]


def get_remaining_coffee():
    return resources["coffee"]


def get_remaining_money():
    return resources["money"]


def get_ingredients_by_coffee_type(coffee_type: str):
    water = MENU[coffee_type]["ingredients"]["water"]
    milk = MENU[coffee_type]["ingredients"]["milk"]
    coffee = MENU[coffee_type]["ingredients"]["coffee"]
    cost = MENU[coffee_type]["cost"]
    return Ingredients(water, milk, coffee, cost)


def make_coffee(ingredients: Ingredients):
    resources["water"] -= ingredients.water
    resources["milk"] -= ingredients.milk
    resources["coffee"] -= ingredients.coffee


def check_payment(cost: float):
    payment_done = False
    print("Please insert coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))

    payment = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    change = payment - cost

    if change > 0:
        resources['money'] += cost
        print(f"Here is your change ${round(change, 2)}")
        payment_done = True
    elif change < 0:
        print("Sorry, you don't have enough money")
    elif change == 0:
        resources['money'] += cost
        payment_done = True

    return payment_done


def check_resources(coffee_type: str):
    ingredients = get_ingredients_by_coffee_type(coffee_type)

    if ingredients.water >= get_remaining_water():
        print('Sorry there is not enough water.')
        order_coffee()
    elif ingredients.milk >= get_remaining_milk():
        print('Sorry there is not enough milk.')
        order_coffee()
    elif ingredients.coffee >= get_remaining_coffee():
        print('Sorry there is not enough coffee.')
        order_coffee()

    if check_payment(ingredients.cost):
        make_coffee(ingredients)
        print(f"Here is your {coffee_type}. Enjoy!")
    order_coffee()


def order_coffee():
    ordered_drink = input('What would you like? (espresso, latte, cappuccino): ')

    if ordered_drink == "report":
        print_report()
        order_coffee()
    elif ordered_drink == "espresso":
        check_resources("espresso")
    elif ordered_drink == "latte":
        check_resources("latte")
    elif ordered_drink == "cappuccino":
        check_resources("latte")
    else:
        print("Sorry wrong option selected.")
        order_coffee()


order_coffee()
