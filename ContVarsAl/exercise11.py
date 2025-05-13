from time import time
import numpy as np

def simXTICauchy(lam):
    return np.tan((np.random.uniform(0,1) - 1/2)*np.pi)*lam

start = time()

for i in range(3):
        Nsim = 10000
        lam = [1, 2.5, 0.3]
        resLam = sum([-lam[i] < simXTICauchy(lam[i]) < lam[i] for _ in range(Nsim)])/Nsim
        print(f"For lam={lam[i]} the result falls into ({-lam[i], lam[i]}): {resLam}")

elapsed = time() - start
print(f"It took {elapsed}s")
