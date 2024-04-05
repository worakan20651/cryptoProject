import ElgamalCrypto
import fileManage
import cryptoMath
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: python your_script.py <input>")
        sys.exit(1)

    content = sys.argv[1]
    fileName = sys.argv[2]

    # print("content in tmp file ",content)
    content = fileManage.readFile(content)

    try:
        with open("publicKeyDirectory.txt",'r') as file:
            # print("FIle open success")
            pbK = file.readline().strip()
            p, g, y = map(int, pbK.strip('()').split(','))
    except FileNotFoundError:
        print("Unable to read file file not found")
    except:
        print("error while read file")

    block_size = cryptoMath.bit10log2(p)

    # print("block size ", block_size)

    # print("Content : ", content)

    # print("(public key) and private key : ",(p,g,y),pvK)
    # signature = digitalSignature.signature(pvK, (p,g,y))

    # print("signature = ", signature)
    
    ci, en_msg = ElgamalCrypto.ElgamalEncrypt((p,g,y),content, block_size)

    print([ci], en_msg)
    fileManage.writeFile(([ci]+ [0] + en_msg), fileName)
    print("-------- Your file is already. --------\n")


print("\n------------ Start process ------------")
main()
