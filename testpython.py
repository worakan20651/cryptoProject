import random
from sympy import mod_inverse

def generate_keypair(p, g):
    # Choose a random private key
    private_key = random.randint(2, p - 2)
    # Calculate public key
    public_key = pow(g, private_key, p)
    return (public_key, private_key)

def encrypt(p, g, public_key, plaintext):
    # Generate a random value k
    k = random.randint(2, p - 2)
    # Calculate ciphertext components
    c1 = pow(g, k, p)
    c2 = (plaintext * pow(public_key, k, p)) % p
    return (c1, c2)

def decrypt(p, private_key, c1, c2):
    # Calculate the shared secret
    shared_secret = pow(c1, private_key, p)
    # Calculate the plaintext
    plaintext = (c2 * mod_inverse(shared_secret, p)) % p
    return plaintext

def string_to_integers(string):
    return [ord(char) for char in string]

def integers_to_string(integers):
    return ''.join([chr(integer) for integer in integers])

# Example usage:

# Choose a prime modulus p and generator g
p = 23
g = 5

# Generate keypair
public_key, private_key = generate_keypair(p, g)
print("Public Key:", public_key)
print("Private Key:", private_key)

# Convert string to integers
plaintext = "Hello, World!"
plaintext_integers = string_to_integers(plaintext)
print("Plaintext (Integers):", plaintext_integers)

# Encrypt the plaintext integers
ciphertext = [encrypt(p, g, public_key, integer) for integer in plaintext_integers]
print("Ciphertext:", ciphertext)

# Decrypt the ciphertext
decrypted_integers = [decrypt(p, private_key, *cipher) for cipher in ciphertext]
print("Decrypted Plaintext (Integers):", decrypted_integers)

# Convert decrypted integers back to string
decrypted_plaintext = integers_to_string(decrypted_integers)
print("Decrypted Plaintext (String):", decrypted_plaintext)
