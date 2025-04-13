
import math
from numpy import random


def monteCarloPi(n:int):
    pointInCircle:float = 0
    for _ in range(1,n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if(x**2+y**2<=1):
            pointInCircle += 1
    return (4* pointInCircle / n)

if __name__ == "__main__":
    print(monteCarloPi(100000))
    print(math.pi)