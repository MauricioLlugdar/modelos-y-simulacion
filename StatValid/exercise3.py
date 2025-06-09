from numpy.random import uniform

data = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]
n = len(data)

def stadKS(arrData: list[float], func):
    arrDataOrd = sorted(arrData)
    D = max([max( (func(arrDataOrd[j]) - (j)/n), (j+1)/n - func(arrDataOrd[j]) ) for j in range(n)])
    return D

d = stadKS(data, lambda x : x)

def ks(Nsim):
    p_val = 0
    for _ in range(Nsim):
        uniVals = [uniform(0,1) for _ in range(n)]
        dSim = stadKS(uniVals, lambda x : x)
        if dSim >= d:
            p_val += 1
    return p_val/Nsim

Nsim = 10000
print(ks(Nsim))