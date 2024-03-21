import cryptoMath
import random
import base64
from PIL import Image
import time

def read_image_with_metadata(file_path):
    filename = file_path
    try:
        # Open the image file
        img = Image.open(filename, mode='r')

        # Convert the image to RGB mode if it's not already in RGB mode
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Convert the image to raw data
        raw_data = img.tobytes()

        # Get metadata if needed
        metadata = img.info

        # Close the image file
        img.close()
        return metadata, raw_data
    
    except FileNotFoundError:
        print("File not found")
        return None, None
    except IOError:
        print("IO Error")
        return None, None

def read_file(file_path):
    filename = file_path
    try:
        with open(filename, "rb") as f:
            content = f.read()
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("IO Error")
    return content

def ElgamalEncrypt(pbK, data):
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
    filename = "cipherText.txt"
    content = str(data)
        
    en_msg = []
    for i in range(len(content)):
        en_msg.append(s * ord(content[i])%p)
        # print("charactor : ",content[i], " into : ", en_msg[i])
    print("ciphertext = ", en_msg)
    
    new_file = f"{filename[:-4]}1{filename[-4:]}"
    
    binary_c1 = bin(c1)[2:]
    byte_c1 = str(binary_c1)
    
    # byte_c1 = bytes([int(binary_c1[i:i+8], 2) for i in range(0, len(binary_c1), 8)])
    print("binary_c1 : ", binary_c1, "\nbyte_c1 : ",byte_c1)
    with open(new_file, 'w') as f:
        f.write(byte_c1)
        
    print("\nwrite ciphertext to file\n")
    try:
        with open(new_file, 'a') as f:
            f.write('\n')
            for c in en_msg:
                print("write : ", str(c))
                f.write(str(c)+" ") 
    except Exception as e:
        print("An error occurred while saving the image:", e)

def ElgamalDecrypt(pvK, filename, p):
    de_msg = []
    first_byte = b''
    print("pvK = ",pvK)
    
    # Read bytes until a space character is encountered
    with open(filename, "rb") as file:
        while True:
            byte = file.read(1)  # Read one byte from the file
            if byte == b' ' or not byte:  # Check if the byte is a space or end of file
                break
            first_byte += byte  # Append the byte to the data string
            
    print(first_byte)
    
    try:
        with open(filename, "rb+") as file:
            # Read the rest of the file content
            rest_of_file = file.read(len(first_byte))
            
    except FileNotFoundError:
        print("File not found")
        return None, None
    except IOError:
        print("IO Error")
        return None, None
        
        
    print("first byte = ", first_byte)
    # Convert byte to binary string without padding
    c1 = int(first_byte)
    print("c1 in byte = ",c1)
    print("c1 = ", c1)
    # Extract components of the private key
    if cryptoMath.mod_exp(c1, p-1, p) == 1:
        x = cryptoMath.mod_exp(c1, p-1-pvK, p)
    else:
        return "Something went wrong with ciphertext or private key" 
    
    # if len(cipher) == 2:
    print("ciphertext before : ",rest_of_file)
            
    for i in range(len(rest_of_file)):
        c = int(rest_of_file[i])
        t = chr((c*x)%p)
        # print("ch is ", t)
        de_msg.append(t)

    print("decipher msg ", de_msg)
    
    new_file = f"{filename[:-4]}2{filename[-4:]}"
    try:
        with open(new_file, 'wb+') as f:
            for c in de_msg:
                f.write(c) 
    except Exception as e:
        print("An error occurred while saving the image:", e)
    
# def ElgamalEncrypt(pbK, data): 
#     # if('.' in data):
#     #     with open(data, 'rb') as file:
#     #         bytes_read = file.read() 
#     # else:
#     #     bytes_read = input()
#     # # method ที่ใช้ในการเข้ารหัส  ให้เข้ารหัสได้ทั้งข้อความจากหน้าจอและไฟล์ประเภทต่างๆ
#     # # Input : key ที่ใช้ในการ...รหัส, Plaintext โดยที่ Plaintext เป็นได้ทั้ง ข้อความที่ได้รับมาจากหน้าจอ หรือ ไฟล์ชนิดต่างๆ
#     # # Output: Ciphertext file
#     p, g, y = pbK
#     k = random.randint(1, p - 2)
    
#     while cryptoMath.gcd(k,p-1) != 1:
#         k = random.randint(1,p-2)
    
#     c1 = cryptoMath.mod_exp(g, k, p)
    
#     # break character into list
#     en_msg = [char for char in data]
    
#     s = cryptoMath.mod_exp(y, k, p)

#     # encrypt data one by one
#     for i in range(len(en_msg)):
#         en_msg[i] = s * ord(en_msg[i])
#         print("charactor : ",data[i], " into : ", en_msg[i])
        
#     print("c1 ", c1, "\nc2 ", en_msg, "\n")
#     return c1,  en_msg

# def ElgamalDecrypt(cipher, pvK, p):
#     dr_msg = []
#     # Unpack the ciphertext tuple
    
    
#     a, b = cipher
#     # print("b : ",b)
    
#     # Extract components of the private key
#     if cryptoMath.mod_exp(a, p-1, p) == 1:
#         x = cryptoMath.mod_exp(a, p-1-pvK, p)
#     else:
#         return "Something went wrong with ciphertext or private key" 
    
#     # print(type(cipher))
    
#     for i in range(len(b)):
#         c = int(b[i])
#         t = chr((c*x)%p)
#         print("ch is ", t)
#         dr_msg.append(t)
#     return dr_msg