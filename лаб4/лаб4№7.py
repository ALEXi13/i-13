# *-* coding: utf-8-*-*
# Лабораторна 4 завдання 7
def Primes(N):
    primes = [i for i in range(1, N+1)]
    primes[0] = 0
    for i in xrange(0, N):
        if primes[i] != 0:
            for j in xrange(i+primes[i],N,primes[i]):
                primes[j] = 0
    return [x for x in primes if x != 0]
print Primes(102)