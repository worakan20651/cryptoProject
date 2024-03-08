import primeGenerate
import ElgamalGenerator
import ElgamalCrypto

req = input("Size and Filename (12 filename.ex) : ")
data = req.split(" ")

prime = 0
while prime == 0:
    print("refiding prime")
    prime = primeGenerate.gen_prime(int(data[0]),data[1])
    
print("prime to use ", prime)

pbK,pvK = ElgamalGenerator.run(prime)


print("(public key) and private key : ",pbK,pvK)

plaintext = "A B "
# byte_values = [ord(char) for char in plaintext]

ciphertext = ElgamalCrypto.ElgamalEncrypt(pbK, plaintext)
print("ciphertext : ",ciphertext, "\n")

plaintext = ElgamalCrypto.ElgamalDecrypt(ciphertext, pvK, prime)
print("plaintext : ",plaintext)

# print("is prime", primeGenerate.is_prime(1775))