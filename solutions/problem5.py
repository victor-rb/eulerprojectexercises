from utitity import page_utils as pu
from utitity import math_utils as mu

_name ,_info, _problem = pu.scrap_problem('https://projecteuler.net/problem=5')

def answer() :

    _total = 20

    while True:
        if mu.is_divisible_by_all(_total, 20):
            break
        else:
            _total += 20

    return _name, _info, _problem, str(_total)