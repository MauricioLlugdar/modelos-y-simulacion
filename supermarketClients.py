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

def counterProb(counter: int)->float:
    match counter:
        case 1:
            return 0.4
        case 2:
            return 0.32
        case 3:
            return 0.28
    return 0    

def waitCounters(counter: int, time: int) -> float:
    timeForEvent: float
    match counter:
        case 1:
            timeForEvent = 3
        case 2:
            timeForEvent = 4
        case 3:
            timeForEvent = 5
    prob4minWait:float = expon.cdf(time, scale=timeForEvent) #P(X_(counter)<4) and this func calcs lambda 1/timeForEvent
    return prob4minWait

def probLess4minWait()->float:
    i:int=0
    wait:float=1
    while i < 1000:
        counterSel:int = clientSelection()
        wait += waitCounters(counterSel, 4)
        i+=1
    return wait/i

def wait4minWhichCounter()-> list[float, float, float]:
    # P(T>4|counter_j)*P(counter_j)/P(T>4) = P(X_j > 4) * P(counter_j) / P(T>4)
    i:int=0
    probCounter_1IfMoreT4min:float=0
    probCounter_2IfMoreT4min:float=0
    probCounter_3IfMoreT4min:float=0
    probWaitMoreT4min = (1-waitCounters(1,4)) * counterProb(1) \
        +(1-waitCounters(2,4)) * counterProb(2) \
        +(1-waitCounters(3,4)) * counterProb(3) # P(T>4)
    amountC1,amountC2,amountC3= 0,0,0
    while i < 100:
        counterSel:int = clientSelection()
        match counterSel:
            case 1:
                probCounter_1IfMoreT4min += (1 - waitCounters(1, 4)) * counterProb(1) / probWaitMoreT4min # P(X_j > 4) * P(counter_j) / P(T>4)
                amountC1+=1
            case 2:
                probCounter_2IfMoreT4min += (1 - waitCounters(2, 4)) * counterProb(2) / probWaitMoreT4min # P(X_j > 4) * P(counter_j) / P(T>4)
                amountC2+=1
            case 3:
                probCounter_3IfMoreT4min += (1 - waitCounters(3, 4)) * counterProb(3) / probWaitMoreT4min # P(X_j > 4) * P(counter_j) / P(T>4)
                amountC3+=1
        i+=1
    print(amountC1)
    print(amountC2)
    print(amountC3)
    probCounter_1IfMoreT4min = probCounter_1IfMoreT4min / amountC1 if amountC1 > 0 else 0
    probCounter_2IfMoreT4min = probCounter_2IfMoreT4min / amountC2 if amountC2 > 0 else 0
    probCounter_3IfMoreT4min = probCounter_3IfMoreT4min / amountC3 if amountC3 > 0 else 0

    return [probCounter_1IfMoreT4min, probCounter_2IfMoreT4min, probCounter_3IfMoreT4min]

if __name__ == "__main__":
    probabilities:list[float, float, float] = wait4minWhichCounter()
    print(f" The probability of waiting less than 4 min was of {probLess4minWait()}")
    print(f" If the client wait for more than 4 min the probability of counter 1: {probabilities[0]}, counter 2: {probabilities[1]} y counter 3: {probabilities[2]}")
