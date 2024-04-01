import cryptoMath
import random
import hashlib
import math

def hash(msg, prime):
    hashed_msg = int.from_bytes(hashlib.sha256(msg.encode()).digest(), byteorder='big')
    
    size = int(math.log10(prime)+1)
    
    # Trim or pad the hash to the desired size
    if len(hashed_msg) > size:
        return hashed_msg[:size]
    elif len(hashed_msg) < size:
        return hashed_msg + b'\x00' * (size - len(hash_value))
    else:
        return hashed_msg


def signature(msg, pbK):
    p,g,y = pbK
    
    hashed_message = hash(str(msg), p)

     # Choose a random number relatively prime to p-1
    while True:
        k = random.randint(2, p - 2)
        if cryptoMath.gcd(k, p - 1) == 1:
            break
        
    # Compute r = g^k mod p
    r = pow(g, k, p) % (p-1)
     # Compute s = (hashed_message - x*r) * k^(-1) mod (p-1)
    k_inv = cryptoMath.mod_inverse(k, p - 1)
    
    s = ((hashed_message + (msg * r)) * k_inv) % (p - 1)

    return (hashed_message,r, s)

def verif(msg, pbK, ):
    p,g,y = pbK
    
    r, s = msg
    
    gx = cryptoMath.mod_exp(g,)
    