import time
from numpy import random
from collections import Counter

def binomialTI(n: int, p: float)-> int:
    c=p/(1-p)
    prob=(1-p)**n
    F = prob
    i=0
    U = random.uniform(0,1)
    while U >= F:
        prob *= c * (n-i) / (i+1)
        F += prob
        i+=1
    return i

def simBinomial(n: int, p: float)-> int:
    ranNum = 0
    successes = 0
    for _ in range(n):
        ranNum = random.uniform(0,1)
        if ranNum < p:
            successes += 1
    return successes

n = 10
p = 0.3
N = 10000 

# time of the TI
start = time.time()
rsBTI = [binomialTI(n,p) for _ in range(N)]
print(Counter(rsBTI).most_common(1)[0][0])
print(f"Proportion of 10 or 0 overall: {((Counter(rsBTI)[0] + Counter(rsBTI)[10])/N)}")
ti_tiempo = time.time() - start

# time of the simBinomial
start = time.time()
rsBTI = [simBinomial(n,p) for _ in range(N)]
print(Counter(rsBTI).most_common(1)[0][0])
print(f"Proportion of 10 or 0 overall: {((Counter(rsBTI)[0] + Counter(rsBTI)[10])/N)}")

ti_simulacion = time.time() - start

print(f"TIBin: {ti_tiempo:.5f} segundos")
print(f"SimBin: {ti_simulacion:.5f} segundos")

