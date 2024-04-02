import primeGenerate
import ElgamalGenerator
import ElgamalCrypto
import fileManage
import digitalSignature
import cryptoMath

try:
    with open("key.txt",'r') as file:
        pbK = file.readline().strip()
        pvK = int(file.readline().strip())
        p, g, y = map(int, pbK.strip('()').split(','))
except:
    print("error while read file")


print("public and privete ", pbK, pvK)

# Read the content from the file
with open("cipher_1.txt", 'r') as file:
    content_str = file.read().strip()

comma_idx = content_str.index(',')

# Remove the parentheses and split the string by comma
content_str = content_str.strip('()')
c1 = int(content_str[:comma_idx-1])
elements = content_str[comma_idx:]

print("content = ", c1)
print("element, " , elements)
# ElgamalCrypto.ElgamalDecrypt(pvK, content, p)