_name = "Even Fibonacci Numbers"
_problem = "Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first $10$ terms will 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,; By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."

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
    
    return _name, _problem, str(_total)