from utitity import page_utils as pu
from utitity import text_utils as tu

_name , _problem = pu.scrap_problem('https://projecteuler.net/problem=4')

def answer() :

    _total = 0

    for first in range(100, 1000):
        for second in range(100, 1000):
            result = first * second
            if tu.is_palindrome(str(result)) and result > _total:
                _total = result
                
    return _name, _problem, str(_total)
