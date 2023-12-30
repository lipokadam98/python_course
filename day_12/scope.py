global_variable = 1


def my_function():
    global_variable = 2


print(global_variable)

# There is no block scope in python so if you create a variable in
# an if statement, while, for loop etc. you can use that variable elsewhere

game_level = 3
enemies = ['Skeleton', 'Zombies', 'Alien']


def increase_enemies():
    # this is how you can modify a global variable, but it is not recommended
    # it is better to have a return statement and modify it after
    global game_level
    if game_level < 5:
        game_level += 1
        new_enemy = enemies[0]


print('new_enemy')

# Global constants

PI = 3.14159
