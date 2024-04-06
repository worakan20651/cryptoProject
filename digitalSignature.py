import cryptoMath
import random
import RWHash
import math

def hash(msg, prime):
    # msg -> binary string representation
    hashed_msg = int.from_bytes(msg.encode(), 'big')
    
    size = int(math.log10(prime)+1)
    
    hash_fuch = RWHash.RWHash(hashed_msg, size)
    
    return hash_fuch


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

def verif(msg, pbK, sign):
    p,g,y = pbK
    
    r, s = sign
    
    if r < 1 or r >= p or s < 1 or s >= (p - 1):
        return False

    w = cryptoMath.mod_inverse(s, p - 1)
    u1 = (hash(msg, p) * w) % (p - 1)
    u2 = (r * w) % (p - 1)
    v = (pow(g, u1, p) * pow(y, u2, p)) % p

    return v == r


# # Example usage:
# # Assume private_key and public_key are generated beforehand
# private_key = (7919, 11, 4327)  # Example private key (p, g, x)
# public_key = (7919, 11, 4529)   # Example public key (p, g, y)

# msg = "Hello, World!"  # Example message

# # Sign the message
# signature = sign(msg, private_key, public_key[0], public_key[1])

# # Verify the signature
# is_valid = verify(msg, signature, public_key)
# print("Signature is valid:", is_valid)