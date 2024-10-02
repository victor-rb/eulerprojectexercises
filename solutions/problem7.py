from utitity import page_utils as pu
from utitity import math_utils as mu

name ,info, problem = pu.scrap_problem('https://projecteuler.net/problem=7')

def answer() :
    _total = 0

    primes = []
    factor = 1

    while len(primes) < 10001 :
        if mu.is_prime(factor) :
            primes.append(factor)
        factor += 1
    
    _total = primes[-1]

    return str(_total)

