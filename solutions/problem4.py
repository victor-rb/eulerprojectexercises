from utitity import page_utils as pu

_name , _problem = pu.scrap_problem('https://projecteuler.net/problem=4')

def answer() :

    _total = 0

    return _name, _problem, str(_total)
