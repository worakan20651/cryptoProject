import os
from PIL import Image
import struct


def writeFile(content, fileName):
    base_name, file_extension = os.path.splitext(fileName)
    new_file = f"{base_name}_{1}{file_extension}"
    print("in print file -- : ", content)
    try:
        with open(new_file, "wb") as file:
            for item in content:
                # Iterate over the list
                if(item == 0):
                    c = b'\x00'
                else:
                    c = struct.pack('>q', item)
                    # c = item.to_bytes(item.bit_length(), byteorder='big')
                    c = remove_null_bytes(c)
                print("write ", c)
                file.write(c)  # Assuming 4-byte unsigned integers
        print("complete writing file ", new_file)
    except Exception:
        print("something went wrong while writing file")

def remove_null_bytes(data):
    return data.replace(b'\x00', b'')

def readFile(fileName):
    try:
        with open(fileName, "r") as file:
            content = file.read()
            # print("content in readFile : ",content)
    except FileNotFoundError:
        print("File not found")
        return None
    except IOError:
        print("file not found")

    return content

def read_Byte_in_File(fileName):

    try:
        print("start read ")
        with open(fileName, "rb") as file:
            binary_string = b''
            byte = file.read(1)
            while byte != b'\x00':
                if not byte:
                    break
                binary_string += byte # Convert byte to character
                # print("test ", binary_string)
                byte = file.read(1)
            
            remaining_bytes = file.read()  # Read the remaining bytes after encountering '\x00'
            return binary_string, remaining_bytes
    except FileNotFoundError:
        print("File not found")
        return None
    except IOError:
        print("file not found")
    


#convert string to binary representation
def strToBin(input_str):
	
    # str_bin = [bin(ord(char))[2:].zfill(8) for char in sPlaintext]
    
    # Convert the string to bytes using the UTF-8 encoding
    input_bytes = input_str.encode('utf-8')

    # Convert each byte to its binary representation
    binary_string = ''.join(format(byte, '08b') for byte in input_bytes)
    
    
    str_bin = "".join(str_bin)
    
    return str_bin


# def decode(aiPlaintext, iNumBits):
#     bytes_array = []
#     k = iNumBits // 8

#     for num in aiPlaintext:
#         for i in range(k):
#             temp = num
#             for j in range(i + 1, k):
#                 temp = temp % (2 ** (8 * j))
#             letter = temp // (2 ** (8 * i))
#             bytes_array.append(letter)
#             num = num - (letter * (2 ** (8 * i)))

#     decodedText = bytearray(b for b in bytes_array).decode('utf-8')

#     return decodedText


# def encode_and_write_image_with_metadata(file_path, iNumBits):
#     metadata, raw_data = read_image_with_metadata(file_path)
#     if raw_data is not None:
#         encoded_data = encode(raw_data, iNumBits)
#         writeFile(str(encoded_data), file_path)
#         return True
#     else:
#         return False


# def decode_image_with_metadata(file_path, iNumBits):
#     content = readFile(file_path)
#     if content is not None:
#         decoded_data = decode(eval(content), iNumBits)
#         return decoded_data
#     else:
#         return None


# Example usage:
# Encode data into image*
# iNumBits = 8  # Number of bits per integer
# encode_and_write_image_with_metadata(file_path, iNumBits)

# Decode data from image
# decoded_data = decode_image_with_metadata(file_path, iNumBits)
# print("Decoded Data:", decoded_data)

# #ReadFile
# file_path = "C:/code/crypto/cryptoProject/cryptoProject/text.txt"
# content = readFile(file_path)
# if content is not None:
#     print("ข้อมูลที่อ่านได้:")
#     print(content)

#Writefile
# file_path = "C:/code/crypto/cryptoProject/cryptoProject/text.txt"
# content_to_write = b""
# writeFile(content_to_write, file_path)
# print("ไฟล์ถูกเขียนเรียบร้อยแล้ว")

