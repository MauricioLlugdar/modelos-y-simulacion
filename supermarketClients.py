from numpy import random
from scipy.stats import expon

def clientSelection() -> int:
    counter: int
    ranNum = random.uniform(0,1)
    if ranNum <= 0.4:
        counter = 1
    elif 0.4 < ranNum <= 0.72:
        counter = 2
    else:
        counter = 3  
    return counter

def waitCounters(counter: int, time: int) -> int:
    timeForEvent: float
    match counter:
        case 1:
            timeForEvent = 3
        case 2:
            timeForEvent = 4
        case 3:
            timeForEvent = 5
    prob4minWait = expon.cdf(time, scale=timeForEvent) #P(X_(counter)<4) and this func calcs lambda 1/timeForEvent
    return prob4minWait

def probLess4minWait()->float:
    i:int=0
    wait:float=1
    while i < 1000:
        counterSel:int = clientSelection()
        wait += waitCounters(counterSel, 4)
        i+=1
    return wait/i

if __name__ == "__main__":

    print(f" The probability of waiting less than 4 min was of {probLess4minWait()}")
