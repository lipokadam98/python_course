import random


def selection_drawer(selection):
    match selection:
        case 'rock':
            print("""
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)
        case 'paper':
            print("""
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            """)
        case 'scissors':
            print("""
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """)


options = ['rock', 'paper', 'scissors']


def check_game_status(user, computer):
    game_status = 'You lose'
    if user == options[1] and computer == options[0] or user == options[2] and computer == options[1] or user == \
            options[0] and computer == options[2]:
        game_status = 'You win'
    elif user == computer:
        game_status = 'It is a draw'
    print(game_status)


user_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))

user_choice = ''
if user_input == 0 or user_input == 1 or user_input == 2:
    user_choice = options[user_input]

if len(user_choice) != 0:
    selection_drawer(user_choice)

    computer_choice = random.choice(options)

    selection_drawer(computer_choice)

    check_game_status(user_choice, computer_choice)

else:
    print('You did not choose a valid option')
