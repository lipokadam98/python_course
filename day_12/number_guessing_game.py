import random

print('Welcome to Number Guessing Game!')
print('I am thinking of a number between 1 and 100.')

difficulty = input('Choose a difficulty level: Type "easy" or "hard": ')
number = random.randint(1, 100)
number_of_guesses = 5

if difficulty == 'easy':
    number_of_guesses = 10

while number_of_guesses > 0:
    print(f'You have {number_of_guesses} attempts remaining to guess the number')
    guess = int(input('Make a guess: '))

    if guess < number:
        print('Too low.')
        number_of_guesses -= 1
    elif guess > number:
        print('Too high.')
        number_of_guesses -= 1
    else:
        print(f'You got it! The answer was {number}.')
        break

if number_of_guesses == 0:
    print(f'You ran out of guesses. The answer was {number}. Game Over!')
