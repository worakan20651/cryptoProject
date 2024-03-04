import random
def GenGenerator(p):
    g = 0
    if(CheckGenerator(g)):
        return g
    
    # Output : g ที่ตรวจสอบแล้วว่าเป็น generator
    return g

def CheckGenerator(g, p):
    
    return True

def ElgamalKeyGen():
    # method ที่ใช้ในการ Generate public และ private key pair
    # Input : ???
    # Output: ???  private key, public key   
    return 


def ElgamalEncrypt(filename): 
    with open(filename, 'rb') as file:
        bytes_read = file.read()
    # method ที่ใช้ในการเข้ารหัส  ให้เข้ารหัสได้ทั้งข้อความจากหน้าจอและไฟล์ประเภทต่างๆ
    # Input : key ที่ใช้ในการ...รหัส, Plaintext โดยที่ Plaintext เป็นได้ทั้ง ข้อความที่ได้รับมาจากหน้าจอ หรือ ไฟล์ชนิดต่างๆ
    # Output: Ciphertext file
    return 


def ElgamalDecrypt():
    # method ที่ใช้ในการถอดรหัสไฟล์ ciphertext
    # Input : key ที่ใช้ในการ...รหัส, Ciphertext file 
    # Output: Plaintext file
    return 

# Extended Euclidean Algorithm to find modular inverse
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Modular inverse function
def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

# Fast modular exponentiation
def mod_exp(base, exp, modulus):
    result = 1
    base = base % modulus
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % modulus
        exp = exp // 2
        base = (base * base) % modulus
    return result
    