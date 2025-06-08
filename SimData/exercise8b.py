from numpy.random import randint

n = 15
N = 1000
data = [5,4,9,6,21,17,11,20,7,10,21,15,13,16,8]

samples = [[data[randint(0,14)] for _ in range(15)] for _ in range(N)]
meanOfEachSample = [sum(sample)/n for sample in samples]
valOfEachEst = [ 
            sum([
                (samples[i][j] - meanOfEachSample[i])**2/(n-1) for j in range(15)
            ])/n  for i in range(N)
]
meanOfAll = sum( 
    valOfEachEst 
    )/(N)

varFe = 1/(N-1) * sum([(valOfEachEst[i]- meanOfAll)**2 for i in range(N)])

print(varFe)