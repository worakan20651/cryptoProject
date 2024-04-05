import ElgamalCrypto
import cryptoMath
import sys
import fileManage
import binascii

def main():
    if len(sys.argv) < 2:
        print("Usage: python your_script.py <input>")
        sys.exit(1)

    content = sys.argv[1]
    newFilename = content[2:]
    content = fileManage.read_Byte_in_File(content)
    # print(content)
    
    c1, msg = content
    print("msg in receive ", msg)
    # print("c1 ,message in receiver ",c1, msg)
    
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
    hex = msg.hex()
    print("hex", hex)
    # binary_list = [bin(byte)[2:].zfill(8) for byte in msg]    
    # binary = "".join(binary_list) 
    print("Check check")
    binary = bin(int(hex, 16))[2:].zfill(8)
    print("bin in recerive ",binary)

    # print("content = ", c1)
    # print("element " , content, "type = ", type(content))
    plaintext = ElgamalCrypto.ElgamalDecrypt(pvK, (c1,binary), p, block_size, newFilename)
    print(plaintext, "type ", type(plaintext))
    print("writing file ", newFilename)
    fileManage.writeFile(plaintext,newFilename)
    print("\n-------- Your file is already. --------\n")


print("\n------------ Start process ------------")
main()

