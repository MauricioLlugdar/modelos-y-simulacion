def genMix(M: int, multi: int, incr: int, seed: int, n: int) -> list[int]:
    ranList: list[int] = [seed]
    newSeed: int = seed
    for i in range(1, n):
        newSeed = ((multi*newSeed) + incr) % M
        ranList.append(newSeed)
    return ranList
    

if __name__ == "__main__":
    try:
        import sys
        M = int(sys.argv[1])
        multi = int(sys.argv[2])
        incr = int(sys.argv[3])
        seed = int(sys.argv[4])
        n = int(sys.argv[5])
        if incr == 0:
            print("The increment is 0 => multiplicative generator")
        else:
            print("The increment is not 0 => mix generator")
        ranList = genMix(M, multi, incr, seed, n)
        print("The ranList generated is: " + str(ranList))
        ranSet = set(ranList)
        print("The size of the list without rep is: " + str(len(ranSet)))

        import matplotlib.pyplot as plt

        # Graficar los pares (X_n, X_{n+1})
        x_vals = list(ranList)[:-1]
        y_vals = list(ranList)[1:]

        plt.figure(figsize=(6, 6))
        plt.scatter(x_vals, y_vals, color='blue', s=25)
        plt.title("Pares (Z_n, Z_{n+1}) del generador")
        plt.xlabel("Z_n")
        plt.ylabel("Z_{n+1}")
        plt.grid(True)
        plt.show()
    except IndexError:
        print("Bad Index")
    except ValueError:
        print("Bad Input")