import sys
from numpy import random

def getRanUnNum()->float:
    return random.uniform(0, 1)

def game(attempts: int)->float:
    games, wins = 0, 0
    
    while games < attempts:
        ranNum = getRanUnNum()
        if ranNum < (1/3):
            score = getRanUnNum() + getRanUnNum() 
        else:
            score = getRanUnNum() + getRanUnNum() + getRanUnNum()
        if score <= 2:
                wins += 1
        games += 1
    
    return (wins/attempts) ## percentage of wins

if __name__ == "__main__":
    print(game(int(sys.argv[1])))