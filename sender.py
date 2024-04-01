import ElgamalCrypto
import fileManage
import cryptoMath

try:
    with open("publicKeyDirectory.txt",'r') as file:
        pbK = file.readline().strip()
except FileNotFoundError:
    print("Unable to read file file not found")
except:
    print("error while read file")
    
# message = input("enter message (file/message) : ")
message = "AB"

if("." in message):
    print("reading your file to encrypt")
    content = fileManage.readFile(message)

else:
    print("reading your message to encrypt")
    content = message
    
# Parse pbK into a tuple of integers
p, g, y = map(int, pbK.strip('()').split(','))

block_size = cryptoMath.bit10log2(p)

print("block size ", block_size)

content = fileManage.encode(content, block_size)

print("Content after encode : ", content)

blocked_content = ElgamalCrypto.block_split(content, block_size)

# print("(public key) and private key : ",(p,g,y),pvK)
# signature = digitalSignature.signature(pvK, (p,g,y))

# print("signature = ", signature)
cipher = str(ElgamalCrypto.ElgamalEncrypt((p,g,y),content))

print("cipher = ", cipher)
# print(ElgamalCrypto.ElgamalDecrypt(pvK, "cipherText1.txt", ))

fileManage.writeFile(cipher, "cipher.txt")