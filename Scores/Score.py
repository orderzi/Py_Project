
def add_score(difficulty,win):
    if win == True:
        points_of_winning = (difficulty * 3) + 5
        return points_of_winning
    else:
        return 0