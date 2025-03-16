from math import ceil, sqrt

def is_prime(num) -> bool:
    """
    Checks if passed number is prime or not

    num -> any whole number

    return -> True if prime, False if not prime
    """
    if num == 1:
        return False
    
    if(sqrt(num) < 2):
        return True
    
    for i in range(2, ceil(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

print(is_prime(1))