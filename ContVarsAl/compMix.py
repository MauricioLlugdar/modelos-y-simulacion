import numpy as np
import math

p = [0.5, 0.3, 0.2]

def exponential(lam: float)-> float:
    U = np.random.uniform(0,1)
    return -math.log(1-U)/lam

def genMix()->float:
    U = np.random.uniform(0,1)
    if U < p[0]:
        return exponential(1/3)
    elif U < p[1] + p[0]:
        return exponential(1/5)
    else:
        return exponential(1/7)
    
if __name__ == "__main__":
    meanMix = np.mean([genMix() for _ in range(100000)])
    print(meanMix)

