import random
from cryptoMath import mod_exp

def run(prime):
    generator = GenGenerator(prime)
    pbK, pvK = ElgamalKeyGen(generator, prime)
    return pbK, pvK

def GenGenerator(p):
    primitiveSet = []
    phi = euler_totient(p)
    factor = prime_factors(phi)
    
    for num in range(2,p-1):
        # print("number ", num)
        if CheckGenerator(num, phi, factor, p):
            # print("Primitive root ", num)
            primitiveSet.append(num)
            
    g = random.choice(primitiveSet)
    # print(primitiveSet)
    return g

def CheckGenerator(n, phi ,factors, p):
    # print("phi ", phi)
    for factor in factors:  
        # print("num : ", n, " | factor : ",factor, " : result ", mod_exp(n, phi//factor, p))
        if mod_exp(n, phi/factor, p) == 1:
            return False
    return True


# find coprime of n
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

# find set of factors(n)
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

def ElgamalKeyGen(g, p):
    # random number between [1,prime-2]
    pvK = random.randint(1, p-2)
    
    y = mod_exp(g, pvK, p)
 
    return (p, g, y), pvK