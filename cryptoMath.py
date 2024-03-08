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