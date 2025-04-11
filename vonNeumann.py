def VonNeumann(u: int) -> int:
    u = ((u ** 2) // 100) % 10000
    return u

if __name__ == "__main__":
    try:
        import sys
        print(VonNeumann(int(sys.argv[1])))
    except ValueError:
        print("Bad Input")