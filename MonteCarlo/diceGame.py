from numpy import random

def rollTheDice()->int:
    ranNum: float= random.uniform(0,0.6)
    dice:int = int(ranNum*10) + 1
    return dice

def gameSim(nSim: int)->float:
    wins: int = 0
    diceA: int = rollTheDice()
    diceB: int = 0
    for _ in range (1,nSim):
        if(diceA == 1 or diceA == 6):
            diceB = rollTheDice()
            wins += 1 if (diceB*2 > 6) else 0
        else:
            diceB = rollTheDice()
            diceC = rollTheDice()
            wins += 1 if (diceB+diceC > 6) else 0

    return (wins/nSim)

if __name__ == "__main__":
    for nSim in [1000, 10000, 100000, 1000000]:
        print(f"P(win in {nSim} simulations)={gameSim(nSim)}")