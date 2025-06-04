from numpy.random import randint


N = 1000
data = [56, 101, 78, 67, 93, 87, 64, 72, 80, 69]
dataLen = len(data) # n
samples = [[data[randint(0,9)] for _ in range(dataLen)] for _ in range(N)] # each sample saved (Only 1000 samples by my decision)
sumOfEachSample = [sum(sample) for sample in samples]
dataMean = sum(data)/dataLen # mu
samplesMean = sum([-5 <= sumOfEachSample[i]/dataLen - dataMean <= 5 for i in range(N)])/N

print(samplesMean)