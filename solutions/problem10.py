from utitity import math_utils as mu
from utitity import page_utils as pu

name ,info, problem = pu.scrap_problem('https://projecteuler.net/problem=10')

def answer() :
    _total = 2
    limit = 2000000

    sieve = [True] * limit
    sieve [0] = sieve[1] = False

    for start in range(2, int(limit ** 0.5) + 1):
        if sieve[start]:
            for multiple in range (start * start, limit, start):
                sieve[multiple] = False

    _total = sum(idx for idx, mu.is_prime in enumerate(sieve) if mu.is_prime)


    return str(_total)
