import numpy as np

def aIntegral(u):
    np.e**u /np.sqrt(2*u)

def exercise2a(Nsim):
    Integral = 0
    for _ in range(Nsim):
        Integral += aIntegral(np.random.uniform(0,1))
    return Integral / Nsim

def bIntegral(u): # Is an even function as we can see
    u**2 * np.exp(-u**2)

def exercise2b(Nsim):
    Integral = 0
    for _ in range(Nsim):
        y = np.random.uniform(0,1)
        Integral += bIntegral(1/y-1) * (1/(y**2))
    return (Integral / Nsim) # Bcs its an integral from -inf to inf and its and even funct