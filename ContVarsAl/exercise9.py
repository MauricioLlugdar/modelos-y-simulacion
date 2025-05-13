import math
import numpy as np

def normal_reject(mu, sigma):
    while True:
        Y1 = -math.log(np.random.uniform(0,1))
        Y2 = -math.log(np.random.uniform(0,1))
        if Y2 >= ((Y1-1) ** 2 / 2):
            if np.random.uniform(0,1) < 1/2:
                return Y1 * sigma + mu
            return -Y1 * sigma + mu
        
def polar(mu, sigma):
    rSquared = -2 * math.log(1-np.random.uniform(0,1))
    theta = 2* math.pi * np.random.uniform(0,1)
    X = math.sqrt(rSquared)*math.cos(theta)
    Y = math.sqrt(rSquared)*math.sin(theta)
    return (X * sigma + mu, Y * sigma + mu)

def normalVariate(mu, sigma):
    NV_MAGICCONST= 4*math.exp(-1/2)/math.sqrt(2.0)
    while 1:
        u1 = np.random.uniform(0,1)
        u2 = 1.0 -np.random.uniform(0,1)
        z = NV_MAGICCONST*(u1-1/2) / u2
        zz = z * z / 4.0
        if zz <= -math.log(u2):
            return mu + z * sigma
        
if __name__ == "__main__":
    mu = 0
    sigma = 1
    print(normal_reject(mu,sigma))
    print(polar(mu,sigma))
    print(normalVariate(mu,sigma))
        