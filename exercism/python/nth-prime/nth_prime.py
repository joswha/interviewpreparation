def primes_sieve(limit):
    primes = dict()
    for i in range(2, limit): 
        primes[i] = True

    for i in primes:
        factors = range(i,limit, i)
        for f in factors[1:]:
            primes[f] = False
            
    return [i for i in primes if primes[i]==True]

def prime(number):
    if number <= 0:
        raise ValueError("Invalid integer")
    else:
        return primes_sieve(199999)[number - 1]

print(prime(5))