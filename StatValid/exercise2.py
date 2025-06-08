from scipy.stats import chi2, binom

# 1a)
prob = 1/6 # Honest Dice
Ns = [158,172,164,181,160,165]
k = len(Ns) - 1 # Degrees of Freedom 
n = 1000
originalT =sum([(Ns[i] - n*prob)**2 /(n*prob) for i in range(6)])
pvalue = 1-chi2.cdf(originalT, k)
print(f"Exercise 1a res = {pvalue}")


# 1b)
def statT(n: int):
    Ns = 0
    N_arr = []
    for j in range(6):
        N_j = binom.rvs(n-Ns, prob/(1-sum([prob for i in range(j)])))
        N_arr.append(N_j)
        Ns += N_j

    T = sum([( (N_arr[i] - n*prob)**2/(n*prob) ) for i in range(6)])
    return T


def estim_pvalue(Nsim):
    bigger = 0
    for i in range(Nsim):
        simT = statT(n)
        if simT > originalT:
            bigger += 1
    return bigger/Nsim

print(estim_pvalue(10000))