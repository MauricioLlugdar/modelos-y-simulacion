from scipy.stats import uniform, expon
from math import exp


data = [86.0, 133.0, 75.0, 22.0, 11.0, 144.0, 78.0, 122.0, 8.0, 146.0, 33.0, 41.0, 99.0]
n = len(data)

def stadKS(arrData: list[float], func):
    arrDataOrd = sorted(arrData)
    D = max([max( (func(arrDataOrd[j]) - (j)/n), (j+1)/n - func(arrDataOrd[j]) ) for j in range(n)])
    return D

Dval = stadKS(data, lambda x : 1 - exp(-x/50))

def ks(Nsim):
    p_val = 0
    
    for _ in range(Nsim):
        uniVals = [uniform.rvs(0,1) for _ in range(n)]
        dSim = stadKS(uniVals, lambda x:x)
        if dSim >= Dval:
            p_val += 1
    return p_val/Nsim

print(ks(10000))