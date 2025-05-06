import math
from numpy import random

def amCombEachPosNum (num: int) -> int:
    
    if(2 <= num <= 7):
        return num-1 
    else:
        return 13-num
        
def probOfEachNum () -> dict[int, float]:
    probEach: dict[int, float] = {}
    for i in range(2,13):
        probEach[i] = amCombEachPosNum(i) / 36 # 36 is the total amounts of combinations
    return probEach

def rollPairOfDices () -> int :
    rollDices : float = random.uniform(0,1)
    floorProbability: float = 0
    resOfRoll: int = 1
    dicesProb = probOfEachNum()
    while floorProbability <= rollDices:
        resOfRoll += 1
        floorProbability += dicesProb[resOfRoll]
    return resOfRoll

def mean(rollsAm: int) -> float:
    valMean: float = 0
    probEach: dict[int, float] = probOfEachNum()
    for _ in range(rollsAm):
        actRes = rollPairOfDices()
        valMean += actRes * probEach[actRes] / rollsAm
    return valMean

def standardDev(rollsAm: int) -> float:
    valMean: float = 0
    probEach: dict[int, float] = probOfEachNum()
    for _ in range(rollsAm):
        actRes = rollPairOfDices()
        valMean += (actRes**2) * probEach[actRes] / rollsAm
    valStdDev = valMean - mean(nSim)**2
    return math.sqrt(valStdDev)
    

if __name__ == "__main__":
    for nSim in [1000, 10000, 100000, 1000000]:
        print(f"Mean in {nSim} throws = {mean(nSim)}")
        print(f"Standard deviation in {nSim} throws = {standardDev(nSim)}")   
