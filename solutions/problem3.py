from utitity import math_utils as mu

_name = "Largest Prime Factor"
_problem = "The prime factors of 13195 are 5, 7, 1 and 29. What is the largest prime factor of the number 600851475143?"


def answer():
    _total = 0

    _number = 600851475143

    _prime_factor = 1

    while (_prime_factor * _prime_factor) <= _number:
        if _number % _prime_factor == 0:
            if mu.is_prime(_prime_factor):
                _total = _prime_factor
        _prime_factor += 2
                
    return _name, _problem, str(_total)
