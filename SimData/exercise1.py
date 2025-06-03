from genNormal import normalvariate
import numpy as np

def exercise1():
    mu = 0
    sigma = 1
    mean = normalvariate(mu,sigma)
    Ssq = 0
    n = 1
    while n <= 100 or np.sqrt(Ssq/n) > 0.1:
        n += 1
        predMean = mean
        mean = predMean + (normalvariate(mu,sigma) - predMean)/(n+1)
        predSsq = Ssq
        Ssq = (1-1/n)* predSsq + (n+1)*(mean - predMean)**2 
    return n, mean, Ssq
        

print(exercise1())