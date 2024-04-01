import math


# Fast modular exponentiation
def mod_exp(base, exp, modulus):
    result = 1
    while exp > 0:
        # check if exp is odd
        if exp % 2 == 1:
            result = (result * base) % modulus
            
        exp = exp // 2
        base = (base * base) % modulus
        
    return result % modulus

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """
    Computes the modular multiplicative inverse of 'a' modulo 'm'
    using the extended Euclidean algorithm and fast modular exponentiation.
    
    Parameters:
        a (int): The base.
        m (int): The modulus.
    
    Returns:
        int: The modular inverse of 'a' modulo 'm', or None if no inverse exists.
    """
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = extended_gcd(b % a, a)
            return (g, x - (b // a) * y, y)
    
    g, x, y = extended_gcd(a, m)
    if g != 1:
        # Modular inverse does not exist
        return None
    else:
        return x % m
    
def bit10log2(n):
    return math.floor(math.log2(n)) + 1
