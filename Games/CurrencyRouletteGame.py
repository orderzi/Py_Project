import random
import requests

def random_amount():
    amount = random.randint(1, 100)
    return amount

def get_money_interval():
    currency = round(requests.get('https://api.fastforex.io/fetch-one?from=USD&to=ILS&api_key=1bfe0676a7-5f1070e946-qqvpia').json()['result']['ILS'], 2)
    return currency

def value_in_shekel(amount, money_inteval):
    value = int(round(amount * money_inteval, 0))
    return value

def get_guess_from_user(amount):
    while True:
        try:
            guess = int(input(f"Guess what is the Value of {amount}$ in ILS:"))
            if guess:
                break
        except ValueError:
            print('Value should be a integer number !\n')
    return guess

def is_user_correct(guess, value_in_shekel, difficulty):
    up_value = value_in_shekel + (5-difficulty)
    down_value = value_in_shekel - (5-difficulty)
    if up_value >= guess >= down_value:
        return True
    else:
        return False

def play_currency_roulette_game(diff_level):
    amount = random_amount()
    money = get_money_interval()
    shekel_value = value_in_shekel(amount, money)
    guess = get_guess_from_user(amount)
    correct = is_user_correct(guess, shekel_value, diff_level)
    if correct == True:
        print('You win the currency roulette game !')
    else:
        print('You lost..try again !')
    return correct


