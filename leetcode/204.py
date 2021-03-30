import math

def sieve(n):
    primes = set(range(2, n))
    for i in range(2, int(math.sqrt(n)) + 1):
        for j in range(i * 2, n, i):
            primes.discard(j)
    return primes

def countPrimes(n):
    return len(sieve(n))

# print(sieve(10))
print(countPrimes(10))