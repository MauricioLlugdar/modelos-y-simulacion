from numpy import random
import math

def integral1(u:float)->float:
    return (1-u**2)**(3/2)

def integral2(u:float)->float:
    return (u / ((u**2) - 1))

def integral3(u:float)->float:
    return (u*(1+u**2)**(-2))

def integral4(u:float)->float:
    return (math.e**(-u**2))

def integral5(u:float, v:float)->float:
    return (math.e**(u+v)**2)

def monteCarlo01(n:int, g)->float:
    sumatory: float = 0
    for _ in range(1, n):
        sumatory += g(random.uniform(0,1))
    value:float = (1/n) * sumatory
    return value
    
#aprox integral on 
def monteCarloIab(n:int, f, b:float, a:float)->float:
    sumatory: float = 0
    for _ in range(1, n):
        sumatory += f(a + (b-a)*random.uniform(0,1))*(b-a)
    value:float = (1/n) * sumatory
    return value


def monteCarloI0inf(n:int, f)->float:
    sumatory: float = 0
   
    for _ in range(1, n):
        ranNum = random.uniform(0,1)
        sumatory += f(1/ranNum-1)*(1/(ranNum**2))
    value:float = (1/n) * sumatory
    return value

def monteCarloDoubleIntegral(n: int, f) -> float:
    sumatory: float = 0
    for _ in range(n):
        x = random.uniform(0, 1)  
        y = random.uniform(0, 1)  
        sumatory += f(x, y)       
    value: float = (1/n) * sumatory  
    return value

if __name__ == "__main__":
    #aprox integral on 0 to 1 of (1-x²)^(3/2)dx
    print(monteCarlo01(1000000, integral1))

    #aprox integral on 2 to 3 of (x)/(x²-1) dx
    print(monteCarloIab(1000000, integral2, 3, 2))

    #aprox integral on 0 to infinite of x*(1+x^2)^(-2) dx
    print(monteCarloI0inf(1000000, integral3))

    int4Res = monteCarloI0inf(1000000, integral4)*2 #2*mC because is an even function
    print(int4Res)

    #aprox integral on 0 to 1 of integral 0 to 1 of e^(x+y)²dx dy
    print(monteCarloDoubleIntegral(100000, integral5))


