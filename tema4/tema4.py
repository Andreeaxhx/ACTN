from sympy import isprime
from math import ceil, sqrt
import random


def legendre(a, n):
    t = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            if n % 8 == 3 % 8 or n % 8 == -3 % 8:
                t = -t
        a, n = n, a

        if a % 4 == 3 % 4 and n % 4 == 3 % 4:
            t = -t
        a = a % n
    return t


def generate(limit):
    p = random.randint(4, limit)
    while not isprime(p):
        p = random.randint(4, limit)

    a = random.randint(2, (p - 2))
    while legendre(a, p) != -1:
        a = random.randint(2, (p - 2))

    return a, p


def skanks(p, alpha, beta):
    # x = i * m + j
    m = ceil(sqrt(p - 1))

    dictionar = {}
    for j in range(m):
        dictionar[pow(alpha, j, p)] = j

    j = -1
    for i in range(0, m):
        aux = (beta * pow(alpha % p, -m * i, p)) % p

        if aux in dictionar.keys():
            j = dictionar[aux]
            break

    print("alpha ^ j = beta * (alpha ^ -m * i)")
    print("alpha = ", alpha)
    print("j = ", j)
    print("beta = ", beta)
    print("m = ", m)
    print("i = ", i)
    print("p = ", p)

    if j != -1:
        return i * m + j
    else:
        return "There is no such value of x."


alpha, p = generate(limit=100)
beta = random.randint(1, p - 1)

x = skanks(p, alpha, p-1)
#x = shanks(13, 7, 146)
print("x = ", x)