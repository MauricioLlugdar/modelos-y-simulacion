import numpy as np
from math import log

def geomTI(p: float)->int:
    U = np.random.uniform(0,1)
    return int(log(1-U)/log(1-p))+1 # attempts until obtaining one success

def GeomRecursive(i: int, rs: float, p: float)->float:
    if(i < 1):
        return rs
    else:
        return GeomRecursive(i-1, (p*(1-p)**(i-1) + rs), p) # P(X = i)

def geomSim(p:float)->int:
    U = np.random.uniform(0,1)
    attempts = 0
    accProb = 0
    while True:
        attempts += 1
        accProb += p*(1-p) ** (attempts-1)
        if(accProb > U):
            return attempts

if __name__ == "__main__":
    for pSim in [0.8, 0.2]:
        arrRsGeoTI:list[int] = [geomTI(pSim) for _ in range(10000)]
        arrRsGeoSim:list[int] = [geomSim(pSim) for _ in range(10000)]
        print(f"The mean using TI is '{np.mean(arrRsGeoTI)}' and the mean using Sim is '{np.mean(arrRsGeoSim)}'")
        

    