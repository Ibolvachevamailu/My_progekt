def amulet_area(a, b, c):
    p = (a + b + c) / 2
    p = int(p)
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(int(S))
    return S

assert amulet_area(3, 4, 5) == 6