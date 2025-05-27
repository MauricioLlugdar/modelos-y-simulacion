import numpy as np

def ejercicio1():
    while 1:
        Y = np.random.uniform(0,1)
        U = np.random.uniform(0,1)
        c = 1.875
        f = lambda x : 30*(x**2-2*x**3+x**4)
        if U < f(Y)/c * (0<=Y <=1):
            return Y
        
def codigoX(p):
    U = np.random.uniform(0,1)
    fRec = lambda q: p*(1-p)**(q-10) # P(X = i)
    ffRec = lambda q: ffRec(q-1)*(1-p) if q>10 else fRec(q) # Funcion recursiva P(X = i+1)
    i=10
    F= ffRec(i)
    while U > F:
        i+=1
        F += ffRec(i)
    return i
        
if __name__ == "__main__":
    Nsim = 10000
    resEj1 = sum([ejercicio1() for _ in range(Nsim)])/Nsim
    print(f"Ej1 E(X)={resEj1}")

    resEj2 = sum([codigoX(0.5) for _ in range(Nsim)])/Nsim
    print(f"Ej2 E(X)={resEj2}")
