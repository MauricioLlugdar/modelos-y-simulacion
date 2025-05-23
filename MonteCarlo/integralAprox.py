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

def integral6(u:float, v:float)->float:
    iy = 1 if u > v else 0
    return (math.e**(-(u+v))*iy)

def integralExam(x:float)-> float:
    return (1 / ( ((x+1)**2) * math.log(x+2) ))

def monteCarlo01(n:int, g)->float:
    sumatory: float = 0
    for _ in range(1, n+1):
        sumatory += g(random.uniform(0,1))
    value:float = (1/n) * sumatory
    return value
    
#aprox integral on 
def monteCarloIab(n:int, f, b:float, a:float)->float:
    sumatory: float = 0
    for _ in range(1, n+1):
        sumatory += f(a + (b-a)*random.uniform(0,1))*(b-a)
    value:float = (1/n) * sumatory
    return value


def monteCarloI0inf(n:int, f)->float:
    sumatory: float = 0
   
    for _ in range(1, n+1):
        ranNum = random.uniform(0,1)
        sumatory += f(1/ranNum-1)*(1/(ranNum**2))
    value:float = (1/n) * sumatory
    return value

def monteCarloDoubleIntegral(n: int, f) -> float:
    sumatory: float = 0
    for _ in range(1,n):
        x = random.uniform(0, 1)  
        y = random.uniform(0, 1)  
        sumatory += f(x, y)       
    value: float = (1/n) * sumatory  
    return value

def monteCarloDoubleIntegral0toInf(n:int,f)->float:
    sumatory: float = 0
    for _ in range(1,n+1):
        x = random.uniform(0, 1)  
        y = random.uniform(0, 1)
        sumatory += f(1/x-1, 1/y-1)*(1/y**2)*(1/x**2)
    value: float = (1/n)* sumatory
    return value

def monteCarloIntegralExam(nSim: int, h)-> float:
    sumatory: float = 0
    for _ in range (1,nSim+1):
        uniNum: float = random.uniform(0,1)
        sumatory += h(1/uniNum -1)*1/(uniNum**2)
    value: float = sumatory * (1/nSim)
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

    #aprox integral on 0 to inf of integral 0 to x of e^(-(x+y))dx dy
    print(monteCarloDoubleIntegral0toInf(100000, integral6))

    #aprox exam integral
    print(monteCarloIntegralExam(1000000, integralExam))