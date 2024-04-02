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
    
    split_cipher = content.replace("(","").replace(")","").split(",")
    print(split_cipher)

    # Convert each byte string to its binary representation
    binary_strings = ElgamalCrypto.byte_to_binary(split_cipher)
    print(binary_strings)


    try:
        with open("key.txt",'r') as file:
            pbK = file.readline().strip()
            pvK = int(file.readline().strip())
            p, g, y = map(int, pbK.strip('()').split(','))
    except:
        print("error while read file")

    block_size = cryptoMath.bit10log2(p)
    c1 = binary_strings[0]
    msg = binary_strings[1]
    c1_blocked = ElgamalCrypto.block_split(c1, block_size)
    blocked_msg = ElgamalCrypto.block_split(msg, block_size)
    print("c1 : ",c1_blocked ," | blocked cipher : ",blocked_msg)
    
    # data = ElgamalCrypto.binary_to_str(blocked_cipher)
    integer_array = ElgamalCrypto.convert_blocked_to_integer(c1_blocked)
    print("C1 ", "".join(integer_array))
    print("public and privete ", pbK, pvK)

    

    # print("content = ", c1)
    # print("element " , content, "type = ", type(content))
    plaintext = str(ElgamalCrypto.ElgamalDecrypt(pvK, c1, content, p, block_size, c1_blocked , blocked_msg))
    print(plaintext)
    return plaintext


print("Start process")
main()

