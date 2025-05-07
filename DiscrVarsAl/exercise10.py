import numpy as np

def accumFunction(n:int)->float:
    accumVal = sum([(1/2)**(j+1)+(1/2)*(2**(j-1)) / 3**j for j in range(1,n+1)])
    return accumVal

def massFunction(n:int)->float:
    return (1/2)**(n+1)+(1/2)*(2**(n-1)) / 3**n

def varDiscAleat()->int:
    U = np.random.uniform(0,1)
    i=1
    F = massFunction(1)
    while U >= F:
        i += 1
        F += massFunction(i)
    return i

if __name__ == "__main__":
    print(np.mean([varDiscAleat() for _ in range(1000)]))
