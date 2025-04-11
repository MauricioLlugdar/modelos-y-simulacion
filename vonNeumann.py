def VonNeumann(u: int) -> int:
    u = ((u ** 2) // 100) % 10000
    return u