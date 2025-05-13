import numpy as np
import math

def addBtwUV():
    return np.random.uniform(0,1) + np.random.uniform(0,1)

def TIBtwUV():
    uRan = np.random.uniform(0,1)
    if uRan < 1/2:
        return math.sqrt(2*uRan)
    elif 1/2 <= uRan < 1:
        return (2-(math.sqrt(8*(1-uRan))/2))
    
def acceptRejUV():
    while 1:
        Y = np.random.uniform(0,2)
        U = np.random.uniform(0,1)
        if Y < 1:
            if U < (Y / (2*(1/2))):
                return Y
        elif 1 <= Y < 2:
            if U < ((2-Y) / (2*(1/2))):
                return Y

if __name__ == "__main__":
    print(np.mean([addBtwUV() for _ in range(10000)]))
    print(np.mean([TIBtwUV() for _ in range(10000)]))
    print(np.mean([acceptRejUV() for _ in range(10000)]))
