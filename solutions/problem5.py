from utitity import math_utils as mu
from utitity import page_utils as pu

name ,info, problem = pu.scrap_problem('https://projecteuler.net/problem=5')

def answer() :

    _total = 20

    primes = [x for x in range(2, _total + 1) if mu.is_prime(x)]
    factors = {prime: 1 for prime in primes}

    for x in range(2, _total + 1):
        for prime, count in mu.prime_factors(x, primes).items():
            factors[prime] = max(count, factors[prime])

    result = 1

    for prime, count in factors.items():
        result *= prime ** count


    return str(result)