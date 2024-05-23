def is_palindrome (text1):
    if text1 == text1[:: -1]:
        return True
    else:
        return False