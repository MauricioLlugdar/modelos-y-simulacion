from numpy.random import uniform
from math import sqrt
from scipy.stats import norm

def simMinN():
    u = uniform(0,1)
    n = 1
    while u < 1 :
        u += uniform(0,1)
        n +=1
    return n

def a_estimate_e():
    mean = simMinN()
    n = 1
    while n <= 1000:
        n += 1
        oldMean = mean
        mean = oldMean + (simMinN()-mean)/(n+1)
    return mean

print(a_estimate_e())

def b_samVar():
    mean = simMinN()
    n = 1
    Ssq = 0
    while n <= 1000:
        n += 1
        oldMean = mean
        mean = oldMean + (simMinN()-mean)/(n+1)
        Ssq = Ssq * (1 - (1/(n-1))) + n*(mean - oldMean)**2
    return Ssq

print(b_samVar())

alpha = 1-0.95
z = norm.ppf(1-alpha/2)
L = 0.025
def c_confInterv():
    d = L /(2*z)
    mean = simMinN()
    Ssq, n = 0, 1
    while n <= 100 or sqrt(Ssq / n) > d:
        n += 1
        oldMean = mean
        mean = oldMean + (simMinN() - oldMean) / n
        Ssq = Ssq * (1 - 1/(n-1)) + n*(mean-oldMean)**2
    return n, mean, Ssq, L

Nsim, mean, Ssq, L = c_confInterv()
print(f"Num of sim was {Nsim}, aprox e = {mean}, variance = {Ssq}, IC=[{mean-L},{mean+L}]")