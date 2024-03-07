import random
import os
from sympy import isprime

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
    print(primitiveSet)
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
    pvK = random.randint(1, p-2)
    
    y = mod_exp(g, pvK, p)
    # method ที่ใช้ในการ Generate public และ private key pair
    # Input : ???
    # Output: ???  private key, public key   
    return (p, g, y), pvK


# def ElgamalEncrypt(filename, p): 
#     if('.' in filename):
#         with open(filename, 'rb') as file:
#             bytes_read = file.read() 
#     else:
#         bytes_read = input()
#     # method ที่ใช้ในการเข้ารหัส  ให้เข้ารหัสได้ทั้งข้อความจากหน้าจอและไฟล์ประเภทต่างๆ
#     # Input : key ที่ใช้ในการ...รหัส, Plaintext โดยที่ Plaintext เป็นได้ทั้ง ข้อความที่ได้รับมาจากหน้าจอ หรือ ไฟล์ชนิดต่างๆ
#     # Output: Ciphertext file
    
#     a = random.randint(1, p - 2)
#     e = (p-1)/2
#     c1 = mod_exp(a, e, p)
#     c2 = (bytes_read * mod_exp(a, e, p)) % p
#     return c1, c2


# def ElgamalDecrypt():
#     # method ที่ใช้ในการถอดรหัสไฟล์ ciphertext
#     # Input : key ที่ใช้ในการ...รหัส, Ciphertext file 
#     # Output: Plaintext file
#     return 

# # Extended Euclidean Algorithm to find modular inverse
# def extended_gcd(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = extended_gcd(b % a, a)
#         return (g, x - (b // a) * y, y)

# # Modular inverse function
# def mod_inverse(a, m):
#     g, x, y = extended_gcd(a, m)
#     if g != 1:
#         raise Exception('Modular inverse does not exist')
#     else:
#         return x % m

# # Fast modular exponentiation
# def mod_exp(base, exp, modulus):
#     result = 1
#     while exp > 0:
#         # check if exp is odd
#         if exp % 2 == 1:
#             result = (result * base) % modulus
            
#         exp = exp // 2
#         base = (base * base) % modulus
        
#     return result % modulus
