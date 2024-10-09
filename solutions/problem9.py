from utitity import page_utils as pu

name ,info, problem = pu.scrap_problem('https://projecteuler.net/problem=9')

def answer() :
    _total = 0

    limit = 10000

    for a in range(1, limit):
        for b in range(a, 500 - a // 2):
            c = 1000 - a - b

            if pow(a, 2) + pow(b, 2) == pow(c, 2):
                _total = (a * b * c)

    return str(_total)
