from genNormal import normalvariate
import numpy as np

def exercise1():
    n = 100
    mu = 0
    sigma = 1
    while 1:
        ranNorm = [normalvariate(mu, sigma) for _ in range(n)]
        S = np.std(a=ranNorm, ddof=1) #ddof indicates that we ar calculating the sample std
        if S/np.sqrt(n) < 0.1:
            return n, sum(ranNorm)/n, S ** 2
        n +=1

print(exercise1())
