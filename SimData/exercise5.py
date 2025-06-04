from numpy.random import uniform
from math import sqrt
from scipy.stats import norm

def biggerThan():
    uOld = 0
    uNext = uniform(0,1)
    n = 1
    while uOld < uNext:
        n += 1
        uOld = uNext
        uNext = uniform(0,1)
    return n

def a_estim_e():
    Ssq=0
    mean = biggerThan()
    n = 1
    while n <= 100 or Ssq/n >= 0.01:
        n+=1
        oldMean = mean
        mean = oldMean + (biggerThan() - oldMean)/n
        Ssq = Ssq * (1-1/(n-1)) + n*(mean-oldMean)**2
    return mean

alpha = 1-0.95
z = norm.ppf(1-alpha/2)
L = 0.1
def b_estim_e():
    d = L/(2*z)
    Ssq=0
    mean = biggerThan()
    n = 1
    while n <= 100 or sqrt(Ssq/n) > d:
        n+=1
        oldMean = mean
        mean = oldMean + (biggerThan() - oldMean)/n
        Ssq = Ssq * (1-1/(n-1)) + n*(mean-oldMean)**2
    return n,mean,Ssq,L

print(a_estim_e())
Nsim, mean, Ssq, L = b_estim_e()
print(f"Num of sim was {Nsim}, aprox e = {mean}, variance = {Ssq}, IC=[{mean-L},{mean+L}]")
