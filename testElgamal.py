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


i = input("What do you want to encrypt?(Filename or message) : ")
if(i.__contains__(".")):
    try:
        with open(i, "rb") as f:
            content = f.read()
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("IO Error")
else:
    content = i
    
plaintext = content
print("Plaintext = ", plaintext, "\n")
# byte_values = [ord(char) for char in plaintext]

print("-------Encryption-------\n")
ciphertext = ElgamalCrypto.ElgamalEncrypt(pbK, plaintext)
print("ciphertext : ",ciphertext, "\n")

print("-------Decryption-------\n")
plaintext = ElgamalCrypto.ElgamalDecrypt(ciphertext, pvK, prime)
try:
    with open(plaintext,'r') as f:
        contain = f.read()
except FileNotFoundError:
    print("file not found")
    
print("plaintext : ",contain)

# print("is prime", primeGenerate.is_prime(1775))