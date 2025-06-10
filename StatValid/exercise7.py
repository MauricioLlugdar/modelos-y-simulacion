from scipy.stats import expon, uniform

n = 30
lam = 1/n
dataGen = [expon.rvs(scale=1) for _ in range(n)] # mean = 1 = scale


def stadKS(arrData: list[float], func):
    arrDataOrd = sorted(arrData)
    D = max([max( (func(arrDataOrd[j]) - (j)/n), (j+1)/n - func(arrDataOrd[j]) ) for j in range(n)])
    return D

Dval = stadKS(dataGen, lambda x : expon.cdf(x=x, scale=1))
print(Dval)


def ks(Nsim):
    p_val = 0
    for _ in range(Nsim):
        uniVals = [uniform.rvs(0,1) for _ in range(n)]
        dSim = stadKS(uniVals, lambda x : x)
        if dSim >= Dval:
            p_val += 1
    return p_val/Nsim

print(ks(10000))

