import ElgamalCrypto
import cryptoMath
import sys
import fileManage

def main():
    if len(sys.argv) < 2:
        print("Usage: python your_script.py <input>")
        sys.exit(1)

    # content = sys.argv[1]
    content = fileManage.read_Byte_in_File('1_text1_1.txt')
    # print(content)
    
    c1, msg = content
    print("c1 ,message in receiver ",c1, msg)
    
    # convert A (Form : bytes) to integer
    c1 = int.from_bytes(c1, byteorder='big')
    print("c1 in receiver ", c1)
    
    # Your code here that uses user_input
    # print("Input received:", content)

    try:
        with open("key.txt",'r') as file:
            pbK = file.readline().strip()
            pvK = int(file.readline().strip())
            p, g, y = map(int, pbK.strip('()').split(','))
    except:
        print("error while read file")

    block_size = cryptoMath.bit10log2(p)

    # Convert binary string to list of integers
    binary_list = [bin(byte)[2:] for byte in msg]    
    binary = "".join(binary_list) 

    # print("content = ", c1)
    # print("element " , content, "type = ", type(content))
    plaintext = str(ElgamalCrypto.ElgamalDecrypt(pvK, (c1,binary), p, block_size))
    print(plaintext)
    return plaintext


print("\n------------ Start process ------------")
main()

