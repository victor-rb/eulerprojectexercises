from utitity import page_utils as pu
from utitity import math_utils as mu

_name , _problem = pu.scrap_problem('https://projecteuler.net/problem=3')

def answer():
    _total = 0

    _number = 600851475143

    _prime_factor = 1

    while (_prime_factor * _prime_factor) <= _number:
        if _number % _prime_factor == 0 and mu.is_prime(_prime_factor):
            _total = _prime_factor
        _prime_factor += 2
                
    return _name, _problem, str(_total)
