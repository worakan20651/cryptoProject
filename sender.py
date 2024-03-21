# import primeGenerate
# import ElgamalGenerator
import ElgamalCrypto

prime = 911
try:
    with open("key.txt",'r') as file:
        pbK = file.readline().strip()
        pvK = int(file.readline().strip())
except:
    print("error while read file")
    
# Parse pbK into a tuple of integers
p, g, y = map(int, pbK.strip('()').split(','))

print("(public key) and private key : ",(p,g,y),pvK)
signature = ElgamalCrypto.signature(pvK, (p,g,y))

print("signature = ", signature)
cipher = ElgamalCrypto.ElgamalEncrypt((p,g,y), "AB"+str(signature))

print("cipher = ", cipher)
# print(ElgamalCrypto.ElgamalDecrypt(pvK, "cipherText1.txt", ))
    