
def is_prime( number ):
    if number == 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    factor = 5

    while factor * factor <= number:
        if number % factor == 0 or number % ( factor + 2 ) == 0:
            return False
        
        factor += 6
    
    return True

def is_divisible_by_all ( number, div_ceil):

    for div in range(1 , div_ceil):
        if number % div != 0:
            return False
    return True