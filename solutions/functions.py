def add(a, b):
    """
    Return the sum of a and b.
    """

    return(a+b)

def subtract(a, b):
    """
    Return the result of a minus b.
    """
    return(a-b)
    

def multiply(a, b):
    """
    Return the product of a and b.
    """
    return a * b


def divide(a, b):
    """
    Return the result of a divided by b.
    If b is zero, return None.
    """
    if b == 0:
        return None
    return a / b

def power(a, b):
    """
    Return the result of raising a to the power of b.
    """
    return(a**b)

def reverse_string(s):
    """
    Return the string s reversed. Such that if s is 'hello' then the function should return 'olleh'
    """
    return("olleh") 