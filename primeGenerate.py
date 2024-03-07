import random

def to_binary(file_content):
    binary = ""
    for byte in file_content:
        binary += format(byte, '08b')
    return binary   

def shuffle_string(s):
    # Shuffle the characters of the string using random.sample()
    shuffled_string = ''.join(random.sample(s, len(s)))
    
    return shuffled_string

def is_prime(n):
     # Special cases for small prime numbers
    if n == 2 or n == 3 or n == 5:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return False

    # Use Lehman Test to check if n is prime
    if lehman_test(n):
        print("Found prime", n)
        return True
    return False
    
def gen_prime(size, file_name):
    file_content = ""
    binary = ""
    try:
        with open(file_name, "rb") as f:
            file_content = f.read()
            binary = to_binary(file_content)
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("IO Error")

    binary = shuffle_string(binary)
    tmp = ""
    prime = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            tmp = binary[i:i + size]
            break

    print("Number generate:", tmp)
    prime = int(tmp, 2)
    print("First number generate:", prime)
    
    bound = (1 << size) - 1
    while not is_prime(prime) and prime < bound:
        if prime % 2 != 0:
            prime += 2
        else:
            prime += 1

    return prime

def lehman_test(n):
    rand = random.Random()
    t = 0

    # Generating a random base less than n
    # Calculating exponent
    e = (n - 1) // 2

    # Iterate to check for different base values for the given number of tries 't'
    while t < 100:
        a = rand.randint(2, n - 3)
        result = fast_expo(a, e, n)
        if result == 1 or result == n - 1:
            pass
        else:
            return False
        t += 1

    # Return positive after attempting
    return True

def fast_expo(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent = exponent >> 1
        base = (base * base) % mod
    return result