from scipy.stats import binom, chi2


prob = [0.31, 0.22, 0.12, 0.10, 0.08, 0.06, 0.04, 0.04, 0.02, 0.01]
frequencies = [188, 138, 87, 65, 48, 32, 30, 34, 13, 2]
totalSpins = sum(frequencies)
k = 10 # vals from 1 to 10

table = [(i+1, frequencies[i]) for i in range(len(frequencies))]

print(f"{'Value':>5} | {'Frequency':>10}")
print("-" * 20)
for val, freq in table:
    print(f"{val:>5} | {freq:>10}")

# H_0: The data has a discrete distribution given by F

expected = [pr*totalSpins for pr in prob]
originalT = sum([(frequencies[i] - expected[i])**2 / expected[i] for i in range(k)])
print(originalT)



def statT(size: int, probArr: list[float]):
    Ns = 0
    N_arr = []
    for j in range(len(probArr)):
        N_j = binom.rvs(size-Ns, probArr[j]/(1-sum([probArr[i] for i in range(j)])))
        N_arr.append(N_j)
        Ns += N_j
    expected = [size * prob for prob in probArr]
    T = sum([(N_arr[i] - expected[i])**2 / expected[i] for i in range(len(probArr))])
    return T

def estim_pvalue(Nsim):
    bigger = 0
    for i in range(Nsim):
        simT = statT(totalSpins, prob)
        if simT > originalT:
            bigger += 1
    return bigger/Nsim

print(estim_pvalue(1000))
dof = len(frequencies) - 1
print(f"Calc chi2 p-value (real) = {1 - chi2.cdf(originalT, dof):5f}")