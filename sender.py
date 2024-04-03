import ElgamalCrypto
import fileManage
import cryptoMath
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python your_script.py <input>")
        sys.exit(1)

    content = sys.argv[1]
    
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

    print("block size ", block_size)

    print("Content : ", content)

    # print("(public key) and private key : ",(p,g,y),pvK)
    # signature = digitalSignature.signature(pvK, (p,g,y))

    # print("signature = ", signature)
    cipher = str(ElgamalCrypto.ElgamalEncrypt((p,g,y),content, block_size))

    print(cipher)
    # print(ElgamalCrypto.ElgamalDecrypt(pvK, "cipherText1.txt", ))


print("Start process")
main()