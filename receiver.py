import primeGenerate
import ElgamalGenerator
import ElgamalCrypto
import fileManage
import digitalSignature
import cryptoMath
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python your_script.py <input>")
        sys.exit(1)

    content = sys.argv[1]
    print(content)
    # Your code here that uses user_input
    print("Input received:", content)

    try:
        with open("key.txt",'r') as file:
            pbK = file.readline().strip()
            pvK = int(file.readline().strip())
            p, g, y = map(int, pbK.strip('()').split(','))
    except:
        print("error while read file")

    block_size = cryptoMath.bit10log2(p)
    
    blocked_cipher = ElgamalCrypto.block_split(content, block_size)
    print("blocked cipher : ",blocked_cipher)
    
    data = ElgamalCrypto.binary_to_str(blocked_cipher)
    print("Data : ",data)
    
    print("public and privete ", pbK, pvK)

    comma_idx = content.index(',')

    # Remove the parentheses and split the string by comma
    content_str = content.strip('()')
    c1 = int(content_str[:comma_idx-1])
    print("C1 : ",c1)
    content = content_str[comma_idx+2:len(content_str)-1]
    print("Content : ",content)

    # print("content = ", c1)
    # print("element " , content, "type = ", type(content))
    plaintext = str(ElgamalCrypto.ElgamalDecrypt(pvK, c1, content, p, block_size))
    print(plaintext)
    return plaintext


print("Start process")
main()