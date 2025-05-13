import numpy as np

fLamI = lambda t: 3 + 4/(t+1) if 0<=t<=3 else 0
fLamII = lambda t: (t-2)**2 - 5*t + 17 if 0<=t<=5 else 0
fLamIII = lambda t : t/2-1 if 2 <= t <= 3 else 1 - t/6 if 3 <= t <= 6 else 0

def poisson_no_homogeneous_slim(T, flam, lam):
    NT=0
    Events = []
    U = 1-np.random.uniform(0,1)
    t = -np.log(U)/lam
    while t <= T:
        V = np.random.uniform(0,1)
        if V < flam(t)/lam:
            NT += 1
            Events.append(t)
        t += -np.log(1-np.random.uniform(0,1))/lam
    return NT, Events

if __name__ == "__main__":
    print(poisson_no_homogeneous_slim(3, fLamI, max([fLamI(i) for i in range(4)]))[0])
    print(poisson_no_homogeneous_slim(3, fLamII, max([fLamII(i) for i in range(6)]))[0])
    print(poisson_no_homogeneous_slim(3, fLamIII, max([fLamIII(i) for i in range(2,7)]))[0])