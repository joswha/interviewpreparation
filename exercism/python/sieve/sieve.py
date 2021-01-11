def primes(limit):
    l = range(2, limit + 1)
    return sorted(set(l).difference(a for i in l for a in l if a != i and a % i == 0))
