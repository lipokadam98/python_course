import random
from typing import List

import black_jack_art

print(black_jack_art.logo)

cards: List[int] = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards: List[int] = []
cpu_cards: List[int] = []
user_score = 0
cpu_score = 0
another = ''
is_user_finished: bool = False


def calculate_score(hand: List[int]) -> int:
    score_sum = sum(hand)
    if score_sum > 21 and 11 in hand:
        score_sum -= 10
    return score_sum


def is_blackjack(hand: List[int]) -> int:
    return (hand[0] == 11 and hand[1] == 10) or (hand[1] == 11 and hand[0] == 10)


def new_game():
    global player_cards, cpu_cards, is_user_finished
    is_user_finished = False
    player_cards = [random.choice(cards), random.choice(cards)]
    cpu_cards = [random.choice(cards), random.choice(cards)]
    calculate_score_player()
    calculate_score_cpu()

    print(f"Your cards : {player_cards}, current score: {user_score}")
    print(f"Computer's first card: {cpu_cards[0]}")


def ask_play_again():
    print_final_scores()
    again = input("Would you like to play again? Type 'yes or 'no'. ").lower()
    if again == "yes":
        new_game()
        start_round()
    else:
        exit(1)


def draw_for_user():
    global player_cards
    player_cards.append(random.choice(cards))
    calculate_score_player()
    print(f"Your cards : {player_cards}, current score: {user_score}")


def draw_for_cpu():
    global cpu_cards
    cpu_cards.append(random.choice(cards))
    calculate_score_cpu()


def calculate_score_player():
    global user_score
    user_score = calculate_score(player_cards)


def calculate_score_cpu():
    global cpu_score
    cpu_score = calculate_score(cpu_cards)


def print_final_scores():
    print(f"Your cards : {player_cards}, final score: {user_score}")
    print(f"Dealer cards : {cpu_cards}, final score: {cpu_score}")


def print_status(status: str) -> None:
    print(status)
    ask_play_again()


def start_round():
    global is_user_finished, another
    another = ''
    if ((is_blackjack(player_cards) and not is_blackjack(cpu_cards))
            or user_score == 21 or cpu_score > 21):
        print_status("You win!")
    elif is_blackjack(cpu_cards) or cpu_score == 21 or user_score > 21:
        print_status("You lose!")
    elif cpu_score == 21 and user_score == 21:
        print_status("Its a draw!")

    if is_user_finished:
        if cpu_score > user_score:
            print_status("You lose!")
        elif cpu_score < user_score:
            print_status("You win!")
        else:
            print_status("Its a draw!")
    else:
        another = input("Do you want another card? Type 'yes' or 'no'.")

    if another == "yes":
        draw_for_user()
        start_round()
    elif another == "no" or is_user_finished:
        is_user_finished = True
        while cpu_score < 16:
            draw_for_cpu()

        start_round()


new_game()
start_round()
