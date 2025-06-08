from scipy.stats import chi2, binom

# 1a)
X = 0.8617
df = 2
p_value = 1 - chi2.cdf(X, df)
print(f"{p_value}")

# 1b)
def statT(n: int, probArr: list[float]):
    Ns = 0
    N_arr = []
    for j in range(len(probArr)):
        N_j = binom.rvs(n-Ns, probArr[j]/(1-sum([probArr[i] for i in range(j)])))
        N_arr.append(N_j)
        Ns += N_j

    T = sum([( (N_arr[i] - n*probArr[i])**2/(n*probArr[i]) ) for i in range(len(probArr) )])
    return T


def estim_pvalue(Nsim):
    originalSample = [141, 291, 132]
    n = sum(originalSample)
    originalProb = [1/4, 1/2, 1/4]
    originalT = sum([ (originalSample[i] - n*originalProb[i])**2/(n*originalProb[i]) for i in range(len(originalSample))])
    bigger = 0
    for i in range(Nsim):
        simT = statT(n,originalProb)
        if simT > originalT:
            bigger += 1
    return bigger/Nsim

print(estim_pvalue(10000))
