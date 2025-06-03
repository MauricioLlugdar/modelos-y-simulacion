import numpy as np

def aIntegral(u):
    return np.e**u /np.sqrt(2*u)

def exercise2a(Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += aIntegral(np.random.uniform(0,1))
    return Integral / Nsim

def bIntegral(u): # Is an even function as we can see
    return u**2 * np.exp(-u**2)

def exercise2b(Nsim):
    Integral = 0
    for _ in range(Nsim):
        y = np.random.uniform(0,1)
        Integral += bIntegral(1/y-1) * (1/(y**2))
    return (Integral / Nsim)*2 # Bcs its an integral from -inf to inf and its and even funct

def sim(func):
    mean = func(1)
    n=1
    Ssq = 0
    while n<100 or np.sqrt(Ssq/n)>=0.01:
        predMean = mean
        mean = predMean + (func(1) - predMean)/(n+1)
        predSsq = Ssq
        Ssq = (1-1/n)* predSsq + (n+1)*(mean - predMean)**2
        n += 1
    return np.sqrt(Ssq)

print(exercise2a(1000))
print(exercise2b(1000))
print(sim(exercise2b))