from collections import Counter
import math
from numpy import random

def PoissonImproved(lamda: float) -> int:
    p = math.exp(-lamda)
    F = p
    for j in range(1, int(lamda) + 1):
        p*= lamda /j
        F += p
    U = random.uniform(0,1)
    if(U >= F):
        j= int(lamda) + 1
        while (U>=F):
            p*= lamda /j
            F += p
            j +=1
        return j-1
    else:
        j = int(lamda)
        while (U < F):
            F -= p
            p *= j/lamda
            j -= 1
        return j+1
    
def Poisson2(lamda: float)-> int:
    U = random.uniform(0,1)
    i=0
    p=math.exp(-lamda)
    F=p
    while U >= F:
        i += 1
        p *= lamda / i
        F = F + p
    return i
    
if __name__ == "__main__":
    N = 1000
    rsPois = [PoissonImproved(10) for _ in range(N)]
    print(f"P(Y>2)={1-(Counter(rsPois)[1]+Counter(rsPois)[0])/N }")

    rsPois = [Poisson2(10) for _ in range(N)]
    print(f"P(Y>2)={1-(Counter(rsPois)[1]+Counter(rsPois)[0])/N }")