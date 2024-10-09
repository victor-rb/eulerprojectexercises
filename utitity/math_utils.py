from math import sqrt


def is_prime( number ):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5

    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
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

def is_pyth_triplets (a, b, c):
    n_sum = (a * a) + (b * b)
    return sqrt(n_sum) == c
