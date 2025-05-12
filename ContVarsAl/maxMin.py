from compMix import exponential

def genMaxMin()->tuple[float, float]:
    X1 = exponential(1)
    X2 = exponential(2)
    X3 = exponential(3)
    M = max(X1,X2,X3)
    m = min(X1,X2,X3)
    return M, m

if __name__ == "__main__":
    distrM = [genMaxMin()[0] for _ in range(10)]
    distrm = [genMaxMin()[1] for _ in range(10)]
    print(distrM)
    print(distrm)