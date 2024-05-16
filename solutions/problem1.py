
_name = "Multiples of 3 or 5"
_problem = "If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23 Find the sum of all the multiples of 3 or 5 below 1000."

def answer() :
    _max = 1000
    _total = 0

    for seq in range(3, _max):
        if seq % 3 == 0 or seq % 5 ==0 :
            _total += seq

    return _name, _problem, str(_total)
