def get_percentage(input_text):
    match input(input_text):
        case '10':
            return 10.0
        case '12':
            return 12.0
        case '15':
            return 15.0
        case _:
            return get_percentage('I said 10, 12 or 15!!! ')


print('Welcome to the tip calculator.')
total = float(input('What was the total bill? $'))

percentage = get_percentage('What percentage tip would you like to give? 10, 12 or 15? ')

total += total * (percentage / 100)

number_of_people = int(input('How many people to split the bill? '))

print(f'Each person should pay: ${round(total / number_of_people, 2)}')
