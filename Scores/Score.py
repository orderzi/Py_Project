import os
from Utils import scores_file


def add_score(difficulty,win):
    scores = open(scores_file, 'r+')
    if os.stat(scores_file).st_size == 0:
        print('file is empty..adding some scores')
        if win == True:
            points_of_winning = (difficulty * 3) + 5
            scores.write(str(points_of_winning))
            scores.close()
            return points_of_winning

    else:
        if win == True:
            read_scores = scores.readlines()
            points_of_winning = int(read_scores[0]) + (difficulty * 3) + 5
            scores.seek(0)
            scores.write(str(points_of_winning))
            scores.truncate()
            scores.close()
            return points_of_winning

