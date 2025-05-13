from exercise12 import poissonEvents
import numpy as np

def tifosi():
    amTifo = 0
    poisEv = poissonEvents(5,1)
    for _ in range(poisEv[0]):
        amTifo += np.random.randint(20,41)
    return amTifo
