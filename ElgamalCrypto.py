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
    
    # print("content before encrypt ", content)
    
    content = block_split(content, block_size)
    # print(len(data))

    # if(data.__contains__(".")):
    #     filename = data
    #     if(data.__contains__("png") or data.__contains__("jpg")):
    #         content = read_image_with_metadata(data)
    #     else:
    #         content = read_file(data)
    # else:
    # print("content aftersplit encrypt ", content)
    
    print("check c1 bin ", c1)
    # test = []
    # test.append(bin(c1)[2:])
    test = str(bin(c1)[2:])
    print("c1 test ",test)

    c1_int = int_to_byte(test)
    print("C1 = ", c1_int)
    
    en_msg = []
    
    for i in content:
        data = int(i,2)
        cipher = (s *data)%p
        bi = bin(cipher)[2:]
        # print("Data : ", data)
        en_msg.append(bi)
        # print("After append : " , data)
    cipher_msg = "".join(en_msg)
    print("cipher message ",cipher_msg)
    
    #from binary to bytesX
    # print("en_msg before ", en_msg)
    en_msg = int_to_byte(cipher_msg)
    
    # # Convert binary strings to integers
    # integers = [int(binary, 2) for binary in en_msg]

    # # Convert integers to bytes
    # byte_string = bytes(integers)
    # print(byte_string)
    
    # en_msg = block_split(c1+cipherJoin, block_size)
    return c1_int, en_msg

def ElgamalDecrypt(pvK,content, p, block_size):
    
    
    de_msg = []

    block_size = cryptoMath.bit10log2(p)
    
    splitted_content = split_list_with_zero(content)
    print("split to ", splitted_content)
    
    print("c1 = ", c1, "type = ", type(c1))
    
    #convert binary to int 
    c1_int = convert_blocked_to_integer(c1_block)
    msg_int = convert_blocked_to_integer(block_msg)
    
    print("c1 : " , c1_int , "msg" , block_msg)
    
    
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
        data = int(i,2)
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
        bi = text[i:i+block_size]
        # blocks.append(bin)
        if(len(bi)==block_size):
            blocks.append(bi)
        else:
            blocks.append(padding.pad_with_zeros(bi, block_size))
    print("block split to ", blocks)
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

def int_to_byte(numbers):
    print("binary to convert:", numbers)
    
    # Pad the binary string to make its length a multiple of 8
    padded_binary_string = numbers.zfill(((len(numbers) + 7) // 8) * 8)
    print("padded = ", padded_binary_string)

    # binary_strings = block_split(padded_binary_string, 8)
    # byte_value = []
    # for binary in binary_strings:
    #     val = binary_to_int(binary)
    #     print("int after binary ", val)
    #     byte_value.append(val.to_bytes(2,'big'))
    
    # print("Byte value:", byte_value)
    
    # Split binary string into bytes
    bytes_list = [padded_binary_string[i:i+8] for i in range(0, len(padded_binary_string), 8)]
    # print("bytes list ", bytes_list)
    # Convert each byte to its integer value and then to bytes
    
    byte_value = ([int(byte,2) for byte in bytes_list])
    print("Byte value:", byte_value)
    
    
    return byte_value

def byte_to_binary(byte_strings):
    binary_strings = []
    for byte_string in byte_strings:
        byte = byte_string.encode()  # Convert byte string to bytes
        binary_string = ''.join(format(byte, '08b') for byte in byte)  # Convert bytes to binary
        binary_strings.append(binary_string)
    return binary_strings

def binary_to_int(binary_string): 
    return int(binary_string,2)

def convert_blocked_to_integer(blocked): 
    print("convert start")
    integer_vals = []
    for binary_string in blocked:
        print("binary_string ", binary_string)
        integer_vals = binary_to_int(binary_string)
        print("convert complet ", integer_vals)
        integer_vals.append(integer_vals)
        
    print("int vals ", integer_vals)
    return integer_vals


def split_list_with_zero(byte_list):
    sublists = [[]]
    for num in byte_list:
        if num == 0:
            if sublists[-1]:
                sublists.append([])
        else:
            sublists[-1].append(num)
    # Remove empty sublists
    sublists = [sublist for sublist in sublists if sublist]
    return sublists