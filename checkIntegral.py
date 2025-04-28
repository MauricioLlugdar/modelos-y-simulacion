import math
import random
import numpy as np
from scipy.integrate import quad


def integralExam(x:float)->float:
    return (math.sqrt(x+math.sqrt(x)))

resultado, error = quad(integralExam, 1, 7)

print(f"Integral: {resultado}")
print(f"Error estimado: {error}")
