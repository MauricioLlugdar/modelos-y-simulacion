from numpy.random import uniform

data = [0.12, 0.18, 0.6, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]
n = len(data)
for i in range(n):
        d = max( (data[i] - (i)/n), (i+1)/n - data[i] )

def ks():
    p_val = 0
    for i in range(n):
        uniVals = [uniform(0,1) for _ in range(n)]
        uniVals.sort()
        dSim = max([max( (uniVals[j] - (j)/n), (j+1)/n - uniVals[j] ) for j in range(n)])
        if dSim <= d:
             p_val += 1
    print(dSim)
    print(d)
    return p_val/n


Nsim = 10000
print(sum([ks() for _ in range(Nsim)])/Nsim)