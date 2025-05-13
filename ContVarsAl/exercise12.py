import numpy as np 

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