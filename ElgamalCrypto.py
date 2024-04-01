import cryptoMath
import random
import hashlib

def ElgamalEncrypt(pbK, content):
    p, g, y = pbK
    k = random.randint(1, p - 2)
    s = cryptoMath.mod_exp(y, k, p)
    
    while cryptoMath.gcd(k,p-1) != 1:
        k = random.randint(1,p-2)
    
    c1 = cryptoMath.mod_exp(g, k, p)
    print("c1 = ",c1)
    # print(len(data))

    # if(data.__contains__(".")):
    #     filename = data
    #     if(data.__contains__("png") or data.__contains__("jpg")):
    #         content = read_image_with_metadata(data)
    #     else:
    #         content = read_file(data)
    # else:
        
    en_msg = []
    for i in content:
        data = int(i,2)
        en_msg.append((s *data)%p)
        # print("charactor : ",content[i], " into : ", en_msg[i])
    print("ciphertext = ", en_msg)
    
    return c1, en_msg

def ElgamalDecrypt(pvK, content, p):
    de_msg = []
    c1, *data = content
    # Convert byte to binary string without padding
    print("c1 in byte = ",c1)
    print("c1 = ", c1, "type = ", type(c1))
    # Extract components of the private key
    if cryptoMath.mod_exp(c1, p-1, p) == 1:
        x = cryptoMath.mod_exp(c1, p-1-pvK, p)
    else:
        return "Something went wrong with ciphertext or private key" 
    
    # if len(cipher) == 2:
    print("ciphertext before : ",content)
            
    for i in range(len(content)):
        t = chr((i*x)%p)
        # print("ch is ", t)
        de_msg.append(t)

    print("decipher msg ", de_msg)
    
    return de_msg


def block_split(text, block_size):
    """
    ฟังก์ชันที่ใช้สำหรับแบ่งข้อความในรูปแบบ block cipher

    :param text: ข้อความที่ต้องการแบ่ง
    :type text: str
    :param block_size: ขนาดของ block ในการแบ่ง
    :type block_size: int
    :return: ลิสต์ของ block ที่แบ่งแยกออกมา
    :rtype: list
    """
    blocks = []
    for i in range(0, len(text), block_size):
        blocks.append(text[i:i+block_size])
    return blocks