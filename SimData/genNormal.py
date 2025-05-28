import numpy as np

NV_MAGICCONST=4*np.exp(-0.5) / np.sqrt(2.0)

def normalvariate(mu, sigma):
    while 1:
        u1 = np.random.uniform(0,1)
        u2 = 1 - np.random.uniform(0,1)
        z = NV_MAGICCONST* (u1-0.5) / u2
        zz = z * z / 4.0
        if zz <= -np.log(u2):
            break
    return mu + z * sigma