from random import randint

# Generates Secret Number
def generate_number(difficulty):
    secret_number = randint(1,difficulty)
    return secret_number

# Get guess from user
def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input(f"Guess a number between 1-{difficulty}"))
            if difficulty >= guess >= 1:
                break
            else:
                print(f'Value should be between 1-{difficulty}')
        except ValueError:
            print('Value should be a number !\n')
    return guess

# Compares guess to secret number
def compare_results(guess,secret_number):
    if guess == secret_number:
        return True
    else:
        return False

# Call all the functions and returns result of True\False
def play_guess_game(dif_level):
    sec_num = generate_number(dif_level)
    call_guess = get_guess_from_user(dif_level)
    result = compare_results(call_guess,sec_num)
    if result == True:
        print('You are the winner of Guess Game !')
    else:
        print('You lost ..Try again ')
    return result

