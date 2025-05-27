import numpy as np
from scipy.optimize import minimize_scalar

# Densidad objetivo f(x)
def f(x):
    return (3/4) * (1 - x**2) if -1 <= x <= 1 else 0

# Densidad auxiliar g(x) = uniforme(-1,1)
def g(x):
    return 0.5 if -1 <= x <= 1 else 0

# Cociente a maximizar
def ratio(x):
    return -f(x) / g(x)  # negativo porque vamos a minimizar

res = minimize_scalar(ratio, bounds=(-1, 1), method='bounded')
c = -res.fun  # revertimos el signo
print(f"Constante c óptima ≈ {c:.4f}")
