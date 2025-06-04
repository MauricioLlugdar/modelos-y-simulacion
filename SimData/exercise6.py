from numpy.random import uniform
from math import sqrt
from scipy.stats import norm

def inCirc(): #Bernoulli
    u = 2 * uniform(0,1)-1
    v = 2 * uniform(0,1)-1
    return (u**2 + v**2 <= 1)

def a_propEst():
    p=0
    n=0
    while n <= 100 or sqrt(p*(1-p)/n) > 0.01:
        n += 1
        p = p + (inCirc() - p)/n
    return n,4*p, sqrt(p*(1-p)/n)

print(a_propEst())


alpha = 1 - 0.95
z = norm.ppf(1-alpha/2)
L=0.1
def b_pi():
    d = L/(2*z)
    p,n=0,0
    while n <= 100 or sqrt(p*(1-p) / n) > d:
        n += 1
        p = p + (inCirc() - p)/n
    return n,4*p,

print(b_pi())
