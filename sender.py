import primeGenerate
import ElgamalGenerator
import ElgamalCrypto
import fileManage
import digitalSignature

try:
    with open("key.txt",'r') as file:
        pbK = file.readline().strip()
        pvK = int(file.readline().strip())
except:
    print("error while read file")
    
# Parse pbK into a tuple of integers
p, g, y = map(int, pbK.strip('()').split(','))

print("(public key) and private key : ",(p,g,y),pvK)
signature = digitalSignature.signature(pvK, (p,g,y))

print("signature = ", signature)
cipher = str(ElgamalCrypto.ElgamalEncrypt((p,g,y),"AB"))+str(signature)

print("cipher = ", cipher)
# print(ElgamalCrypto.ElgamalDecrypt(pvK, "cipherText1.txt", ))

fileManage.writeFile(cipher, "cipher.txt")