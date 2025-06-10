from scipy.stats import binom, chi2

data = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
size = len(data)
nVals = 8
p = sum(data)/(nVals*size)

groups = [
    [0,1,2],
    [3,4],
    [5,6],
    [7,8]
]

freqEachGroup = [
    sum(data.count(k) for k in group) for group in groups
]

probabilities = [
    sum(binom.pmf(k, nVals, p) for k in group) for group in groups
]

expected = [size * prob for prob in probabilities]

originalT = sum([(freqEachGroup[i] - expected[i])**2 / expected[i] for i in range(len(groups))])

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
        simT = statT(size, probabilities)
        if simT > originalT:
            bigger += 1
    return bigger/Nsim

print("Seen freq:", freqEachGroup)
print("Expected freq:", expected)
print("Statistical chi2:", originalT)
print("p-valor (simulado):", estim_pvalue(10000))

grado_chi = len(groups) - 1 - 1
print(f"Calc chi2 p-valor (real) = {1 - chi2.cdf(originalT, grado_chi):5f}")