from utitity import page_utils as pu
from utitity import math_utils as mu

_name ,_info, _problem = pu.scrap_problem('https://projecteuler.net/problem=6')

def answer() :
    _total = 0

    sum_of_square = 0
    square_of_the_sum = 0

    for nat_number in range(1, 101):
        sum_of_square += nat_number ** 2
        square_of_the_sum += nat_number

    square_of_the_sum = square_of_the_sum ** 2

    _total = square_of_the_sum - sum_of_square

    return _name, _info, _problem, str(_total)