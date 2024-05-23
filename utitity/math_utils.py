
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