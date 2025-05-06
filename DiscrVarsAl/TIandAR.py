import math
from numpy import random
from poisson import PoissonImproved
from scipy.stats import poisson
from collections import Counter

lam = 0.7
k=10

def massFunctionEX8(x_j: float) -> float:
    F=0
    summative = sum((lam**j) * (math.e**(-lam)) / math.factorial(j) for j in range(k+1))
    if summative: 
        F = ((((lam**x_j) * math.e**(-lam)) / math.factorial(x_j) )/ (summative))
    return F

def invTransf()-> int:
    U = random.uniform(0,1)
    x_i = 0
    F = massFunctionEX8(x_i)
    while U >= F:
        x_i += 1
        F += massFunctionEX8(x_i)
    return x_i

def accRejec()-> float:
    c = max(
            massFunctionEX8(x_j)/(poisson.pmf(x_j, lam)) for x_j in range(k+1)
        )
    
    while True:
        Y: int = PoissonImproved(lam)
        U: float = random.uniform(0,1)
        # P(X = x_j)/P(Y = y_j) <= c
        if Y > k:
            continue
        
        if U < (massFunctionEX8(Y) / (c * poisson.pmf(Y, lam))):
            return Y

if __name__ == "__main__":
    #P(X>2)
    rsTI = [invTransf() for _ in range(1000)]
    rsAR = [accRejec() for _ in range(1000)]
    print(sum(Counter(rsTI)[i] for i in range(2)))
    print(sum(Counter(rsAR)[i] for i in range(2)))    
    print(f"P(X>2)={1 - sum(Counter(rsTI)[i] for i in range(2))/1000}")
    print(f"P(X>2)={1 - sum(Counter(rsAR)[i] for i in range(2))/1000}")