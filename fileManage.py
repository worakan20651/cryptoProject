import os
from PIL import Image


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


def writeFile(content, fileName):
    base_name, file_extension = os.path.splitext(fileName)
    new_file = f"{base_name}_{1}{file_extension}"
    try:
        with open(new_file, "w") as file:
            file.write(content)
    except Exception:
        print("something went wrong while writing file")


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

