import random

'''The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
ontains the previous Hi-score. You need to write a program to update the Hi-
score whenever the game() function breaks the Hi-score.'''

def game():
    print('You are playing game....')
    Score = random.randint(1,100)
    with open("Hi-score.txt") as file:
        Hiscore = file.read()
        if(Hiscore != ""):
            Hiscore = int(Hiscore)
        else:
            Hiscore = 0
    print(f"Your Score {Score}")
    if(Score>Hiscore):
        with open("Hi-score.txt","w")as file:
            file.write(str(Score))

    return Score

game()

