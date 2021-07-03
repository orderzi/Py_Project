from Games import CurrencyRouletteGame, GuessGame, MemoryGame
from Scores import Score
import requests

def welcome(name):
    name_output = (f"Hello {name}  and welcome to the World of Games (WoG). Here you can find many cool games to play\n")
    print(name_output)
    return name

# choose game from 1-3 and return the choice
def get_game():
    while True:
        try:
            choose_game = int(input('Please Choose game to play\n'
                                    '1.Memory game - a sequence of number will appear for 1 seconds and you have to guess it back\n'
                                    '2.Guess Game - guess a number and see if you chose like computer\n'
                                    '3.Currency Roulette - try and guess the value of a random amount of USD in ILS\n'))
            if 3 >= choose_game >= 1:
                break
            else:
                print('Value should be between 1-3\n')
        except ValueError:
            print('Value should be number !\n')
    return choose_game

# choose difficulty from 1-5 and return the choice
def get_difficulty():
    while True:
        try:
            choose_diff = int(input('Please choose game difficulty from 1 to 5'))
            if 5 >= choose_diff >= 1:
                break
            else:
                print('Value should be between 1-5 !')
        except ValueError:
            print('Value should be number !\n')
    return choose_diff

# load the selected game by the parameters of game and difficulty
def load_game():
    game = get_game()
    difficulty = get_difficulty()
    data = {"Game": game,
            "Difficulty": difficulty}
    if game == 1:
        play_memory_game = MemoryGame.play_memory_game(difficulty)
        data['Score'] = play_memory_game
    elif game == 2:
        play_guess_game = GuessGame.play_guess_game(difficulty)
        data['Score'] = play_guess_game
    elif game == 3:
        play_currency_game = CurrencyRouletteGame.play_currency_roulette_game(difficulty)
        data['Score'] = play_currency_game
    return data

def send_to_api(user,points):
    url = 'http://localhost:5001/scores'
    data = {'user': str(user), 'score': int(points)}
    post = requests.post(url, json=data)
    print(post)
    return post

if __name__ == '__main__':
   user = welcome('iKarmi')
   load_games = load_game()
   difficulty = load_games['Difficulty']
   is_win = load_games['Score']
   adding_score = Score.add_score(difficulty, is_win)
   api_post = send_to_api(user, adding_score)











