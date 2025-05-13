import numpy as np

def CAUCHY(lam):
    while 1:
        U = np.random.uniform(0, np.sqrt(1/(np.pi)))
        V = np.random.uniform(-np.sqrt(1/(np.pi)), np.sqrt(1/(np.pi)))
        if U**2 + V**2 < 1/np.pi:
            return lam*V/U


if __name__ == "__main__":
    Nsim = 10000
    lam = [1,2.5,0.3]
    
    for i in range(3):
        resLam = sum([-lam[i] < CAUCHY(lam[i]) < lam[i] for _ in range(Nsim)])/Nsim
        print(f"For lam={lam[i]} the result falls into ({-lam[i], lam[i]}): {resLam}")
