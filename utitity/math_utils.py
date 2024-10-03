from math import floor


def is_prime( number ):

    for x in range(2, floor(number ** 0.5) + 1):
        if number % x == 0:
            return False
    return True

def prime_factors(number, primes):
    result = {prime: 0 for prime in primes}
    for prime in primes:
        while number % prime == 0:
            result[prime] += 1
            number = number / prime
            print(result)
    return result

def is_divisible_by_all ( number, div_ceil):

    for div in range(1 , div_ceil):
        if number % div != 0:
            return False
    return True