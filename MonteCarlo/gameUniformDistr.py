import sys
from numpy import random

def getRanUnNum()->float:
    return random.uniform(0, 1)

def game(attempts: int)->float:
    games, wins = 0, 0
    
    while games < attempts:
        ranNum = getRanUnNum()
        if ranNum >= 0.5:
            score = getRanUnNum() + getRanUnNum() + getRanUnNum()
        else:
            score = getRanUnNum() + getRanUnNum()
        if score >= 1:
                wins += 1
        games += 1
    
    return (wins/attempts) ## percentage of wins

if __name__ == "__main__":
    print(game(int(sys.argv[1])))