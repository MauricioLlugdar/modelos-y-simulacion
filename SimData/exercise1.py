from genNormal import normalvariate
import numpy as np

def exercise1():
    mu = 0
    sigma = 1
    ranNorm = [normalvariate(mu, sigma), normalvariate(mu, sigma)]
    n = 2
    while True:
        S = np.std(a=ranNorm, ddof=1)
        if (S/np.sqrt(n) < 0.1) and (n >= 101):
            return n, sum(ranNorm)/n, S ** 2
        n += 1
        ranNorm.append(normalvariate(mu, sigma))

print(exercise1())