import math
import random

def maxProd():
    prod = 1
    amNum = 0
    while prod >= math.e**(-3):
        prod *= random.uniform(0, 1)
        amNum += 1
    return amNum - 1

def amOfProd(n_simul: int) -> float:
    total = 0
    for _ in range(n_simul):
        total += maxProd()
    return total / n_simul

def probEspecificN(N:int, n_simul:int)-> float:
    totalN = 0
    for _ in range(n_simul):
        amNum = maxProd()
        if(amNum == N):
            totalN += 1
    return totalN / n_simul


if __name__ == "__main__":
    print(amOfProd(1000000))
    for i in range(0,6):
        print(f"P(N={i})={probEspecificN(i,1000000)}")
    