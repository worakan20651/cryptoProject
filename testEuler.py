def euler_totient(n):
    result = n  # Initialize result as n

    # Consider all prime factors of n and subtract their multiples from result
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    # If n has a prime factor greater than sqrt(n)
    if n > 1:
        result -= result // n

    return result

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

def primitive_root(phi,n):
    primitiveSet = []
    primeFactor = prime_factors(phi)
    # print("phi : ",phi, " | n", n)
    for num in range(2,n-1):
        # print("number ", num)
        if is_Primitive_root(num, phi, primeFactor, n):
            # print("Primitive root ", num)
            primitiveSet.append(num)
    return primitiveSet

def is_Primitive_root(n, phi ,factors, p):
    # print("phi ", phi)
    for factor in factors:  
        print("num : ", n, " | factor : ",factor, " : result ", mod_exp(n, phi//factor, p))
        if mod_exp(n, phi/factor, p) == 1:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(n)
    return factors


# Example usage:
p = 11  # Example prime number
primitiveRootNum = euler_totient(p)
if primitiveRootNum:
    print("Set of primitive roots modulo", p, ":", primitive_root(primitiveRootNum,p))
else:
    print("No primitive roots found.")
# print(euler_totient(10))