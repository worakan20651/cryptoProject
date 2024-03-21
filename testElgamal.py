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


# print("(public key) and private key : ",pbK,pvK)
# pbK = (911, 296, 620)
# pvK = 584


# plaintext = input("What do you want to encrypt?(Filename or message) : ")
# if(plaintext.__contains__(".")):
#     if(plaintext.__contains__("png") or plaintext.__contains__("jpg")):
#         content = ElgamalCrypto.read_image_with_metadata(plaintext)
#     else:
#         content = ElgamalCrypto.read_file(plaintext)
#     ElgamalCrypto.ElgamalEncryption(pbK, content)
#     print("-------Decryption-------\n")
#     # plaintext = ElgamalCrypto.ElgamalDecrypt(i, pvK, prime)
# else:
#     content = plaintext
#     print("-------Encryption-------\n")
#     ElgamalCrypto.ElgamalEncryption(pbK, content)
#     print("-------Decryption-------\n")
#     # plaintext = ElgamalCrypto.ElgamalDecrypt(ciphertext, pvK, prime)

cipher = ElgamalCrypto.ElgamalEncrypt(pbK, "AB")
print(ElgamalCrypto.ElgamalDecrypt(pvK, "cipherText1.txt", prime))
    
# plaintext = content
# print("Plaintext = ", plaintext, "\n")
# byte_values = [ord(char) for char in plaintext]

# print("ciphertext : ",ciphertext, "\n")

    
# print("plaintext : ",plaintext)

# print("is prime", primeGenerate.is_prime(1775))