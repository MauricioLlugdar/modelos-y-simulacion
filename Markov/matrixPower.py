import numpy as np

Q = np.array([
    [0.25, 0.5, 0.25],
    [0.5, 0, 0.5],
    [0.5, 0, 0.5]
])

QN = np.linalg.matrix_power(Q, 4)
print(QN)
