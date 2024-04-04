import ElgamalCrypto
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
    
    
    # Convert binary string to list of integers
    byte_list = [int(content[i:i+8], 2) for i in range(0, len(content), 8)]
    print("byte = ",byte_list)    

    # print("content = ", c1)
    # print("element " , content, "type = ", type(content))
    plaintext = str(ElgamalCrypto.ElgamalDecrypt(pvK, byte_list, p, block_size))
    print(plaintext)
    return plaintext


print("Start process")
main()

