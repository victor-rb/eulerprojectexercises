from utitity import page_utils as pu

name ,info, problem = pu.scrap_problem('https://projecteuler.net/problem=2')

def answer() :
    _total = 2
    _res = 0
    _num_a = 1
    _num_b = 2

    while _res < 4000000:
        _res = _num_a + _num_b
        _num_a = _num_b
        _num_b = _res
        if(_res % 2 == 0):
            _total += _res
    
    return str(_total)