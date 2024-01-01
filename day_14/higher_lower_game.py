import random

import game_data
import higher_lower_art

DATA = game_data.data
LOGO = higher_lower_art.logo
VS_LOGO = higher_lower_art.vs


def compare_two(choice_a, current_score):
    a = choice_a
    b = random.choice(DATA)

    if a['name'] == b['name']:
        while a['name'] == b['name']:
            b = random.choice(DATA)

    a_followers = a['follower_count']
    b_followers = b['follower_count']
    print(f"Compare A : {a['name']}, a {a['description']}, from {a['country']}.")
    print(VS_LOGO)
    print(f"Against B : {b['name']}, a {b['description']}, from {b['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ")

    has_more_followers = 'A' if a_followers > b_followers else 'B'

    if choice == has_more_followers:
        current_score += 1
        print(f'You are right! Current score: {current_score}')
        if has_more_followers == 'A':
            compare_two(a, current_score)
        else:
            compare_two(b, current_score)
    else:
        print("Sorry you lose!")
        another = input("Do you want to play again? Type 'yes' or 'no'.")

        if another == "yes":
            compare_two(random.choice(DATA), 0)
        

print(LOGO)
compare_two(random.choice(DATA), 0)
