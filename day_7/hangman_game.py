import random


def check_winning_state(word):
    won = True
    for literal in word:
        if literal == '_':
            won = False

    return won


def get_lives(life_left):
    match life_left:
        case 6:
            print("""
            _______
            |     |
            |     
            |     
            |    
            |
         ___|___
        |       |""")
        case 5:
            print("""
            _______
            |     |
            |     O
            |     
            |    
            |
         ___|___
        |       |""")
        case 4:
            print("""
            _______
            |     |
            |     O
            |     |
            |    
            |
         ___|___
        |       |""")
        case 3:
            print("""
            _______
            |     |
            |     O
            |    /|
            |    
            |
         ___|___
        |       |""")
        case 2:
            print("""
            _______
            |     |
            |     O
            |    /|\\
            |    
            |
         ___|___
        |       |""")
        case 1:
            print("""
            _______
            |     |
            |     O
            |    /|\\
            |    / 
            |
         ___|___
        |       |""")
        case 0:
            print("""
                   _______
                   |     |
                   |     O
                   |    /|\\
                   |    / \\
                   |
                ___|___
               |       |""")


word_list = ["aardvark", "baboon", "camel"]

print("""
  _   _                                         
 | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | |_| |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
 |  _  | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                     |___/                       
""")
chosen_word = random.choice(word_list)
winning_state = False
lives = 6
guessed_word = []
for letter in chosen_word:
    guessed_word.append('_')

while lives > 0:
    letter_was_correct = False
    guess = input('Guess a letter:').lower()
    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
            letter_was_correct = True
            guessed_word[i] = guess
    winning_state = check_winning_state(''.join(guessed_word))
    if winning_state:
        print('You won!')
        lives = 0

    if not letter_was_correct:
        lives -= 1

    get_lives(lives)

    if lives <= 0 and not winning_state:
        print('Game over!')
    print(''.join(guessed_word))
