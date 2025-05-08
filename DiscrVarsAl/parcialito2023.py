import numpy as np

p = [0.05, 0.1, 0.2, 0.3, 0.35]

def ejercicio1a():
    while(True):
        Y = int(np.random.uniform(0,1)*5)
        U = np.random.uniform(0,1)
        c = 0.35/(1/5) #max(P(X=x_j)/P(Y=x_j))
        if U < p[Y] / (c *(1/5)):
            return Y
        
def ejercicio1b(N):
    return sum([ejercicio1a() for _ in range(N)])*(1/N)

print(ejercicio1b(1000))

def ejercicio2a():
    p.reverse()
    U = np.random.uniform(0,1)
    i = 0
    F = p[i]
    while U >= F:
        i += 1
        F += p[i]
    return i

def ejercicio2b(N):
    return sum([ejercicio2a() for _ in range(N)])*(1/N)

print(ejercicio2b(1000))

#Esperanza exacta Sum de i=0 hasta n de x_i * P(X = x_i) //En la consigna dice que i va de 0 a 4
def ejercicio3():
    return sum([(i)*(p[i]) for i in range(5)])

print(ejercicio3())