import math
import numpy as np
from collections import Counter

#ex 7

def tiOneOverX():
    U = np.random.uniform(0,1)
    return math.e**U

def accRejecOneOverX():
    while 1:
        Y = np.random.uniform(1,math.e)
        U = np.random.uniform(0,1)
        f = 1/Y
        g = 1/(math.e-1)
        c = math.e-1
        if U < f/(g*c):
            return Y

if __name__ == "__main__":
    sampleTI = [tiOneOverX() for _ in range(10000)]
    sampleAccRej = [accRejecOneOverX() for _ in range(10000)]
    print(np.mean(sampleTI))
    print(np.mean(sampleAccRej))

    #P(X <= 2)
    lessOrEq2 = sum([sampleAccRej[i] <= 2 for i in range(10000)])/10000
    print(lessOrEq2)