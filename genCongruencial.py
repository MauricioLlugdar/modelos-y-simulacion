def genMix(M: int, multi: int, incr: int, seed: int, n: int) -> list[int]:
    ranSet: list[int] = [seed]
    newSeed: int = seed
    for i in range(1, n):
        newSeed = ((multi*newSeed) + incr) % M
        ranSet.append(newSeed)
    return ranSet

if __name__ == "__main__":
    try:
        import sys
        M = int(sys.argv[1])
        multi = int(sys.argv[2])
        incr = int(sys.argv[3])
        seed = int(sys.argv[4])
        n = int(sys.argv[5])
        ranSet = genMix(M, multi, incr, seed, n)
        print("The ranSet generated is: " + str(ranSet))
        print("The size of the list is: " + str(len(ranSet)))
    except IndexError:
        print("Bad Index")
    except ValueError:
        print("Bad Input")