MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}

cash = 0

def report():
    print(f'Water: {resources['water']} ml')
    print(f'Milk: {resources['milk']} ml')
    print(f'Coffee: {resources['coffee']} g')
    print(f'Money: ${cash}')

def coins():
    quarters = int(input('How many Quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    total_value = (quarters*0.25) + (dimes*0.1) + (nickles*0.05) + (pennies *0.01)
    return total_value

def resource_check(bev):
    for resource in MENU[bev]['ingredients']:
        if MENU[bev]['ingredients'][resource] > resources[resource]:
            print("Insufficient resources")
            return False
        else:
             return True

def transaction(money,bev):
    if MENU[bev]['cost'] > money:
        print("Insufficient Funds. Money Refunded")
        return None
    elif MENU[bev]['cost'] == money:
        print("Transaction Successful")
        return money
    else:
        change = money - MENU[bev]['cost']
        print(f'Here is ${change} in change.')
        money = money - change
        return money
def make_coffee(bev):
    for resource in MENU[bev]['ingredients']:
        if MENU[bev]['ingredients'][resource] in resources:
            resources[resource] = resources[resource] - MENU[bev]['ingredients'][resource]






machine_on = True
while machine_on:
    user_coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if user_coffee == 'off':
        machine_on = False
    elif user_coffee == 'report':
        report()
    for drink in MENU:
        if user_coffee == drink:
            price = MENU[drink]['cost']
            resource_check(user_coffee)
            print(f'A {drink} costs ${price}. Enter the your Coins')
            user_money = coins()
            cash += transaction(user_money,user_coffee)
            for resource in MENU[user_coffee]['ingredients']:
                resources[resource] = resources[resource] - MENU[user_coffee]['ingredients'][resource]
            print(f'Here is your {user_coffee}. Enjoy!')



