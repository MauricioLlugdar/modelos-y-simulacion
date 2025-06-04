from numpy.random import uniform
from math import pi, sin, sqrt
from scipy.stats import norm

f_aux_1 = lambda x : sin(x)/x
f_i = lambda U : pi * f_aux_1(pi + pi*U)

f_aux_2 = lambda x : 3 / (3 + x**4)
f_ii = lambda U : (1/U**2) * f_aux_2(1/U - 1)


z = norm.ppf(0.975) # 1 - alpha/2

def aproxByL(f, Nsim):
    L = 0.001
    n, Ssq = 1, 0
    mean = f(uniform(0,1))
    k = 2 if Nsim else 1
    while n <= 100 or (k * z * sqrt(Ssq / n ) > L)* Nsim or Nsim>n: # If Nsim = 0 => automatic error
        n += 1
        predMean = mean
        mean = predMean + (f(uniform(0,1)) - predMean) / n
        Ssq = Ssq * (1-1/(n-1)) + n*(mean - predMean)**2
    return n, mean, Ssq, L
    

def print_table(results):
    print(f"{'N° de sim.':>12} | {'Ī':>9} | {'S':>9} | {'IC(95%)':>23}")
    print("-" * 62)
    for N, mean, S, IC in results:
        IC_str = f"[{mean - IC:.4f}, {mean + IC:.4f}]"
        print(f"{(N if N != 0 else n):>12} | {mean:>9.4f} | {S:>9.4f} | {IC_str:>23}")

results = []
for f in [f_i, f_ii]:
    print(f"Monte carlo aproximation for {'f_i' if f == f_i else 'f_ii'}:")
    print("-" * 62)
    for N in [0, 1000, 5000, 7000]:
        n, mean, S, IC = aproxByL(f, N)
        results.append((N, mean, S, IC))
    print_table(results)
    results.clear()
    print("\n")


