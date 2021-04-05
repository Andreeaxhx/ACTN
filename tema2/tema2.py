from Cryptodome.Util.number import inverse
from time import perf_counter


def DecimalToBinary(n):
    return bin(n).replace("0b", "")

# trebuie sa calculam y^d mod n eficient (CRT)


def rsa_crt_multiprime(y):

    phi = (p - 1) * (q - 1) * (r - 1)
    d = pow(e, -1, phi)

    b1 = pow(y % p, d % (p - 1), p)
    b2 = pow(y % q, d % (q - 1), q)
    b3 = pow(y % r, d % (r - 1), r)

    x1 = b1 % p
    c = ((b2 - x1) * inverse(p, q)) % q
    x2 = x1 + p * c

    d = ((b3 - x2) * inverse(p * q, r)) % r
    x3 = x2 + p * q * d

    return x3


def rsa_crt_multipower(y):

    phi = p * (p - 1) * (q - 1)
    d = pow(e, -1, phi)
    p2 = p * p
    x0 = pow(y % p, d % (p - 1), p)
    xq = pow(y % q, d % (q - 1), q)

    first = (y - pow(x0, e, p2)) // p
    second = inverse(e * pow(x0, e - 1, p), p)
    x1 = (first * second) % p

    xp2 = x1 * p + x0

    sol1 = xp2 % p2
    c = ((xq - sol1) * inverse(p2, q)) % q

    sol2 = sol1 + p2 * c

    return sol2

p = 8560130647072146891548007257107097292672473260101015101256906059553463448579564694754937215621594339939202146155346955524454206447453255723489922464294019
q = 7930258804805855514518534155736512799996014546061768344341971145776229613732619086878916960511852747523101349777304612220797782032603520415243082481650597
r = 12205334515714503011112551529699976938774509931284898075857641208947518432008734341554225602041805034405156222091671860293705737724245293398544189354844627

e = 3846393823

y = 48761539940486768790697951968441053167086423529120379009399989923982917278530780108524481919294548305561552133247376067350664771674488982501980538923179804440135482761541868213581098181220801732284669971107195377327445661261746882474615837238429855596647745621191046720648860759474615170945636435027382702345930153884587334870109990234396501579


n = p * q * r
phi = (p - 1) * (q - 1) * (r - 1)
d = pow(e, -1, phi)

start_multiprime = perf_counter()
output = rsa_crt_multiprime(y)
stop_multiprime = perf_counter()

start_library = perf_counter()
result = pow(y, d, n)
stop_library = perf_counter()

print("y^d mod n (multiprime RSA): ", output)
print("y^d mod n (library):        ", result)

print("execution time for multiprime RSA: ", stop_multiprime-start_multiprime)
print("execution time for y^d mod n:      ", stop_library-start_library)
print("multiprime is", (stop_library-start_library)/(stop_multiprime-start_multiprime), "times faster")
print()


n = p * p * q
phi = p * (p - 1) * (q - 1)
d = pow(e, -1, phi)

start_multipower = perf_counter()
output2 = rsa_crt_multipower(y)
stop_multipower = perf_counter()

start_library = perf_counter()
result = pow(y, d, n)
stop_library = perf_counter()

print("y^d mod n (multiprime RSA): ", output2)
print("y^d mod n (library):        ", result)

print("execution time for multipower RSA: ", stop_multipower-start_multipower)
print("execution time for y^d mod n:      ", stop_library-start_library)
print("multipower is", (stop_library-start_library)/(stop_multipower-start_multipower), "times faster")


