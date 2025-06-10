from scipy.stats import norm
import math
import random

def rt(df): # df grados de libertad
    x = random.gauss(0.0, 1.0)
    y = 2.0*random.gammavariate(0.5*df, 2.0)
    return x / (math.sqrt(y/df))

#t-student DISTRIBUTION
origSamplesSz = [10,20,100,1000] # Size of samples
dof = 11
data = [[rt(df=dof) for _ in range(origSamplesSz[i])] for i in range(len(origSamplesSz))]

#H_0: normal distribution N(0,1)

def stadKS(n, arrData: list[float], func):
    arrDataOrd = sorted(arrData)
    D = max([max( (func(arrDataOrd[j]) - (j)/n), (j+1)/n - func(arrDataOrd[j]) ) for j in range(n)])
    return D

 

def ks(Nsim, Dval, n):
    p_val = 0
    for _ in range(Nsim):
        normVals = [norm.rvs(0,1) for _ in range(n)]
        dSim = stadKS(n, normVals, lambda x : norm.cdf(x=x,loc=0, scale=1))
        if dSim >= Dval:
            p_val += 1
    return p_val/Nsim

print(f"{'Sample size':>12} | {'D statistic':>12} | {'p-value':>10}")
print("-" * 40)
for i, origN in enumerate(origSamplesSz):
    Dval = stadKS(origN, data[i], lambda x : norm.cdf(x=x, scale=1, loc=0))
    Nsim = 1000
    p_val = ks(Nsim, Dval, origN)
    print(f"{origN:>12} | {Dval:>12.4f} | {p_val:>10.4f}")
