import cryptoMath
import random
import padding

def ElgamalEncrypt(pbK, content, block_size):
    p, g, y = pbK
    k = random.randint(1, p - 2)
    
    while cryptoMath.gcd(k,p-1) != 1:
        k = random.randint(1,p-2)
        
    s = cryptoMath.mod_exp(y, k, p)
    
    c1 = cryptoMath.mod_exp(g, k, p)
    print("c1 = ",c1)
    
    print("s = ", s, "\nk = ", k)
    
    print("content before encrypt ", content )
    
    content = block_split(content, block_size)
    # print(len(data))

    # if(data.__contains__(".")):
    #     filename = data
    #     if(data.__contains__("png") or data.__contains__("jpg")):
    #         content = read_image_with_metadata(data)
    #     else:
    #         content = read_file(data)
    # else:
    print("content aftersplit encrypt ", content )
        
    en_msg = []
    en_msg.append(c1)
    for i in content:
        data = int(i,2)
        print("Data : ", data)
        en_msg.append((s *data)%p)
        # print("charactor : ",content[i], " into : ", en_msg[i])
    
    # print("en_msg before ", en_msg)
    en_msg = int_to_binary_to_byte(en_msg)
    print("message ",en_msg)
    
    # Convert binary strings to integers
    integers = [int(binary, 2) for binary in en_msg]

    # Convert integers to bytes
    byte_string = bytes(integers)
    print(byte_string)
    
    # en_msg = block_split(c1+cipherJoin, block_size)
    return byte_string

def ElgamalDecrypt(pvK, c1, content, p, block_size):
    de_msg = []

    block_size = cryptoMath.bit10log2(p)
    
    print("c1 = ", c1, "type = ", type(c1))
    
    if cryptoMath.mod_exp(c1, p-1, p) == 1:
        x = cryptoMath.mod_exp(c1, p-1-pvK, p)
        print("x : ", x)
    else:
        return "Something went wrong with ciphertext or private key" 
    
    # blocked_content = block_split(str_to_binary(content), block_size)
    print("ciphertext before : ",content)
    content = [int(x) for x in content.split(',')]
    # print("type of cipher now", type(content))
    
    for i in content:
        # data = int(i,2)
        t = (i*x)%p
        print("ch is ", t)
        
        bi = bin(t)[2:].zfill(block_size-1)
        print("de_bi : ", bi)
        de_msg.append(bi)

    print("decipher msg ", de_msg)
    
    de_msg =  ''.join(de_msg)
    print("after join : ", de_msg)
    
    decipher_block = block_split(de_msg, 8)
    
    print("blocked ", decipher_block)
    
    result = cipher_to_pt(decipher_block)
    
    print("decipher_block ", result)
    
    return result


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
        bin = text[i:i+block_size]
        if(len(bin)==block_size):
            blocks.append(bin)
        else:
            blocks.append(padding.pad_with_ones(bin,block_size))
    return blocks

def str_to_binary(data):
    # Extract the tuple from the string
    list_str = data[2:len(data)-1]

    print("check in str_to_binary : ", list_str, "type ", type(list_str))
    # Split the tuple string by comma and convert each element to integer
    list_elements = list_str.split(',')
    
    print("check in str_to_binary : ", list_elements, "type ", type(list_elements))
    list_elements = [int(x) for x in list_elements]
    
    # Convert each integer to binary representation
    binary_list = [bin(x)[2:] for x in list_elements]
    
    return ''.join(binary_list)
    
# print(str_to_binary("15296, 6159, 10828, 0, 2296, 0]"))

def binary_to_str(data):
   
    # Convert binary strings to characters  
    characters = [int(binary, 2) for binary in data]
    
    return characters

def cipher_to_pt(data):
   
    # Convert binary strings to characters  
    characters = [ord(int(binary, 2)) for binary in data]
    
    return characters

def int_to_binary_to_byte(numbers):
    byte_arrays = []
    binary_list = [bin(number)[2:] for number in numbers]
    print("Binary representation ", binary_list)

    binary_string = ''.join(binary_list)
    print("Bin ", binary_string)
  
    # Split the binary string into substrings of 8 bits (1 byte)
    split_bit = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]

    print("split bit ", split_bit)
    
    byte_arrays = []
    for byte_string in split_bit:
        print(byte_string, " ", len(byte_string))
        if(len(byte_string) < 8):
            byte_string = padding.pad_with_zeros(byte_string)
        byte_arrays.append(byte_string)
    # print("sending : ",byte_arrays)
    
    return byte_arrays

    # return byte_arrays
    
