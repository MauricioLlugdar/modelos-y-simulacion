import numpy as np

def urnMethod(p):
    A = []
    j=0
    k = 100
    while j<=3:
        for _ in range(int(k*p[j])):
            A.append(j)
        j += 1
    U = np.random.uniform(0,1)
    print(int(k*U))
    return A[int(k*U)]

def exerc2():
    U = np.random.uniform(0,1)
    if U <= 1/3:
        return np.log(3*U) #np.log = ln
    else:
        return np.log(3/2 * (1-U))/(-2)
    
def exerc3():
    while 1:
        Y = np.random.uniform(-1,1)
        f = lambda x: (3/4)*(1-x**2) if -1<=x<=1 else 0
        g = lambda x: 1/(1+1) if -1<=x<=1 else None
        c = 3/2
        U = np.random.uniform(0,1)
        if U < f(Y)/(c*g(Y)):
            return Y
        
def exerc4a():
    throwCoin = lambda: "Heads" if np.random.uniform(0,1) < 1/3 else "Tails"
    fRs = throwCoin()
    count = 1
    while 1:
        nowRs = throwCoin()
        count += 1
        if fRs != nowRs:
            return count
        
def exerc4c():
    while 1: 
        Y = int(np.log(1-np.random.uniform(0,1))/(np.log(1-1/3)))+1
        f = lambda n : (2**(n-1)+2)/3**n
        g = lambda n : (1/3)*(1-1/3)**(n-1)
        c=1
        if np.random.uniform(0,1) < f(Y)/(c*g(Y)) * (Y >= 2):
            return Y

if __name__ == "__main__":
    probabilities = [0.32,0.21,0.33,0.14]
    print(urnMethod(probabilities))

    Nsim = 10000

    resEx2 = sum([exerc2() <= 1 for _ in range(Nsim)]) # P(X<=1)
    print(f"P(X<=1)={resEx2/Nsim}")

    ##4a
    resEx4a = sum ([exerc4a() == 4 for _ in range(Nsim)]) #P(X=4)
    print(f"P(X=4)={resEx4a/Nsim}")

    resEx4c = sum ([exerc4c() == 4 for _ in range(Nsim)]) #P(X=4)
    print(f"P(X=4)={resEx4c/Nsim}")