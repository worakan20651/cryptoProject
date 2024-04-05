import cryptoMath
import random
import padding

def ElgamalEncrypt(pbK, content, block_size):
    print("Block size = ",block_size)
    p, g, y = pbK
    k = random.randint(1, p - 2)
    
    while cryptoMath.gcd(k,p-1) != 1:
        k = random.randint(1,p-2)
        
    s = cryptoMath.mod_exp(y, k, p)
    
    c1 = cryptoMath.mod_exp(g, k, p)
    print("c1 = ",c1)
    
    print("s = ", s, "\nk = ", k)
    
    # print("content before encrypt ", content)
    print("before content : ",content)
    content = block_split(content, block_size)
    # print("content split ", content)
    
    en_msg = []
    
    for i in content:
        data = int(i,2)
        print("data = ",data)
        cipher = (s *data)%p
        print("cipher in encrypt ", cipher)
        bi = bin(cipher)[2:]
        print("bi ", bi)
        en_msg.append(padding.pad_with_zeros(bi, block_size))
        
    print("wait ",en_msg)

    cipher_msg = "".join(en_msg)
    print("check this ", cipher_msg)

    en_msg = binary_to_byte(cipher_msg)
    print("en_msg : ", en_msg)
    
    return c1, en_msg

def ElgamalDecrypt(pvK,cipher, p, block_size, fileName):
    block_size = cryptoMath.bit10log2(p)
    c1, msg = cipher
    print("in decrypt")
    unpad = padding.unpad_zeros(msg)
    
    split_msg = block_split(unpad, block_size)
    print(split_msg) 
    
    if cryptoMath.mod_exp(c1, p-1, p) == 1:
        x = cryptoMath.mod_exp(c1, p-1-pvK, p)
        print("x : ", x)
    else:
        return "Something went wrong with ciphertext or private key" 
    content = []
    
    de_msg = []
    for i in split_msg:
        data = int(i,2)
        t = (data*x)%p
        print("i = ",data, " ch is ", t)
        # print("ch is ", t)
        de_msg.append(t)

    # from integer to binary
    de_msg_binary = int_to_binary(de_msg)
    # from binary split to each byte
    if('txt' in fileName):
        de_msg_split = block_split(de_msg_binary, 7)
    else:
        de_msg_split = block_split(de_msg_binary, 8)
    # print("decipher split ", de_msg_split)
    
    de_msg_byte = []
    for msg in de_msg_split:
        num = int(msg,2)
        de_msg_byte.append(num)
        
    print("plaintext ", de_msg_byte)
    
    return de_msg_byte


def block_split_without_fill(text, block_size=8):
    blocks = []
    padlen = 0
    for i in range(0, len(text), block_size):
        print("len ", len(text), " idx : ", i)
        if(i+block_size < len(text)):
            bi = text[i:i+block_size]
        else:
            bi = text[i:len(text)]
        i+=block_size
        blocks.append(bi)
    print("block split to ", blocks)
    return blocks


def block_split(text, block_size=8):
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
    padlen = 0
    for i in range(0, len(text), block_size):
        bi = text[i:i+block_size]
        # blocks.append(bin)
        print("len ", len(text), " idx : ", i)
        if(len(bi)==block_size):
            blocks.append(bi)
        else:
            pad = padding.pad_with_zeros(bi, block_size)
            # print("blocking pad ",pad)
            blocks.append(pad)
    print("block split to ", blocks)
    return blocks

def binary_to_byte(numbers):
    # print("binary to convert:", numbers)
    
    # Pad the binary string to make its length a multiple of 8
    # padded_binary_string = padding.pad_with_zeros(numbers)
    padded_binary_string = block_split(numbers)
    # print("padded = ", padded_binary_string)
    
    # Convert each byte to its integer value and then to bytes
    byte_value = ([int(byte,2) for byte in padded_binary_string])
    # print("Byte value:", byte_value)
    return byte_value

def binary_to_byte_with_fill(numbers):
    # print("binary to convert:", numbers)
    
    # Pad the binary string to make its length a multiple of 8
    # padded_binary_string = padding.pad_with_zeros(numbers)
    padded_binary_string = block_split_with_fill(numbers)
    # print("padded = ", padded_binary_string)
    
    # Convert each byte to its integer value and then to bytes
    byte_value = ([int(byte,2) for byte in padded_binary_string])
    # print("Byte value:", byte_value)
    return byte_value

def binary_to_int(binary_string): 
    return int(binary_string,2)

def unpadded_binary(binary):
    bi_unpad = padding.unpad_zeros(binary)
    print("bi_unpadded ", bi_unpad)
        
    print("unpadded")
    return bi_unpad

def int_to_binary(int_list):
    binary_list = [bin(byte)[2:] for byte in int_list]
    binary = "".join(binary_list)
    print("bin of byte ", binary)

    return binary

