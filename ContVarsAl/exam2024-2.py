import numpy as np
from scipy.integrate import quad

def ejercicio2(uVal=None): #optional parameter
    if uVal == None:
        U = np.random.uniform()
    else:
        U = uVal
    if U < 2/3:
        return (3/2 * U)**(2/3)
    else:
        return (3*U -1)

def poissonEvents(lam, T):
    t=0
    NT=0
    Events = []
    while t < T:
        U = 1- np.random.uniform(0,1)
        t += -np.log(U)/lam
        if t <= T:
            NT += 1
            Events.append(t)
    return NT, Events

fLam = lambda t: (
    5+t*5 if 0<= t <3
    else
    20 if 3<= t <=5
    else
    30-2*t if 5<t<=9
    else 0
)

def hot_dog(T):
    interv = [1,2,6,8,9]
    lam = [10,15,20,18,14]
    j=0
    t=-np.log(1-np.random.uniform(0,1))/lam[j]
    NT=0
    Events = []
    while t <= T:
        if t <= interv[j]:
            V = np.random.uniform(0,1)
            if V < fLam(t)/lam[j]:
                NT += 1
                Events.append(t)
            t += -np.log(1-np.random.uniform(0,1))/lam[j]
        else:
            t = interv[j] + (t-interv[j])*lam[j] /lam[j+1]
            j+=1
    return NT, Events

# Exact E(X)
I1, _ = quad(lambda t: 5 + 5*t, 0, 3)
I2, _ = quad(lambda t: 20, 3, 5)
I3, _ = quad(lambda t: 30 - 2*t, 5, 9)

if __name__ == "__main__":
    uVals = [0.2, 0.5, 0.8]
    Nsim = 10000
    
    for i in range(3):
        print(ejercicio2(uVals[i]))
    
    res = [ejercicio2() for _ in range(Nsim)]

    #P(X>4)
    xBigOne = sum([res[i]>1 for i in range(Nsim)])
    print(f"P(X>1)={xBigOne/Nsim}")

    print(f"E(X)= {sum([hot_dog(9)[0] for _ in range(Nsim)])/Nsim} montecarlo")
    print(f"E(X)= {I1+I2+I3} exacta")

    
    

