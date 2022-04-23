from random import randint


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def primRoots(modulo):
    coprime_set = {num for num in range(1, modulo) if gcd(num, modulo) == 1}
    return [g for g in range(1, modulo) if coprime_set == {pow(g, powers, modulo)
            for powers in range(1, modulo)}]


if __name__ == '__main__':

    n = 23
    g = primRoots(n)[0]

    Ax = randint(2, n)
    By = randint(2, n)

    AX = int(pow(g, Ax, n))
    BY = int(pow(g, By, n))

    Ak = int(pow(BY, Ax, n))
    Bk = int(pow(AX, By, n))

    print("Ak:", Ak)
    print("Bk:", Bk)

    k = Ak
