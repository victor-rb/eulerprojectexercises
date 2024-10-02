from utitity import page_utils as pu

name ,info, problem = pu.scrap_problem('https://projecteuler.net/problem=1')

def answer() :
    _max = 1000
    _total = 0

    for seq in range(3, _max):
        if seq % 3 == 0 or seq % 5 ==0 :
            _total += seq

    return str(_total)