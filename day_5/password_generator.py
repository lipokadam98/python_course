# Password Generator Project
import random


def random_selector_from_array(string_array, number_of_letters):
    random_strings = []
    for i in range(number_of_letters):
        random_strings.append(random.choice(string_array))

    return random_strings


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

random_letters = random_selector_from_array(letters, nr_letters)
random_numbers = random_selector_from_array(numbers, nr_numbers)
random_symbols = random_selector_from_array(symbols, nr_symbols)

print(random_symbols)
print(random_letters)
print(random_numbers)

output = ''.join(random_letters) + ''.join(random_symbols) + ''.join(random_numbers)

print(output)
# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = ''
while len(password) != nr_letters + nr_symbols + nr_numbers:
    rand_switch = random.randint(1, 3)

    match rand_switch:
        case 1:
            if len(random_numbers) > 0:
                password += random.choice(random_numbers)
                random_numbers.pop()
        case 2:
            if len(random_letters) > 0:
                password += random.choice(random_letters)
                random_letters.pop()
        case 3:
            if len(random_symbols) > 0:
                password += random.choice(random_symbols)
                random_symbols.pop()

print(password)
