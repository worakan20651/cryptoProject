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
    except FileNotFoundError:
        print("File not found")
        return None
    except IOError:
        print("file not found")

    return content


#encodes bytes to integers mod p.  reads bytes from file
def encode(sPlaintext, iNumBits):
	
    byte_array = bytearray(sPlaintext, 'utf-16')

	#z is the array of integers mod p
    z = []

	#each encoded integer will be a linear combination of k message bytes
	#k must be the number of bits in the prime divided by 8 because each
	#message byte is 8 bits long
    k = iNumBits//8

	#j marks the jth encoded integer
	#j will start at 0 but make it -k because j will be incremented during first iteration
    j = -1 * k
	#num is the summation of the message bytes
	# i iterates through byte array
	# Iterate through the byte array
 
    for i in range(len(byte_array)):
    # If i is divisible by k, start a new encoded integer
        if i % k == 0:
            j += k
            z.append("")

        # Add the byte as binary string
        byte_bin = bin(byte_array[i])[2:].zfill(8)  # Convert byte to binary string
        z[j // k] += byte_bin

		#example
				#if n = 24, k = n / 8 = 3
				#z[0] = (summation from i = 0 to i = k)m[i]*(2^(8*i))
				#where m[i] is the ith message byte

	#return array of encoded integers
    return z


def decode(aiPlaintext, iNumBits):
    bytes_array = []
    k = iNumBits // 8

    for num in aiPlaintext:
        for i in range(k):
            temp = num
            for j in range(i + 1, k):
                temp = temp % (2 ** (8 * j))
            letter = temp // (2 ** (8 * i))
            bytes_array.append(letter)
            num = num - (letter * (2 ** (8 * i)))

    decodedText = bytearray(b for b in bytes_array).decode('utf-8')

    return decodedText


def encode_and_write_image_with_metadata(file_path, iNumBits):
    metadata, raw_data = read_image_with_metadata(file_path)
    if raw_data is not None:
        encoded_data = encode(raw_data, iNumBits)
        writeFile(str(encoded_data), file_path)
        return True
    else:
        return False


def decode_image_with_metadata(file_path, iNumBits):
    content = readFile(file_path)
    if content is not None:
        decoded_data = decode(eval(content), iNumBits)
        return decoded_data
    else:
        return None


# Example usage:
# Encode data into image*
iNumBits = 8  # Number of bits per integer
# encode_and_write_image_with_metadata(file_path, iNumBits)

# Decode data from image
# decoded_data = decode_image_with_metadata(file_path, iNumBits)
# print("Decoded Data:", decoded_data)

#ReadFile
file_path = "C:/code/crypto/cryptoProject/cryptoProject/text.txt"
content = readFile(file_path)
if content is not None:
    print("ข้อมูลที่อ่านได้:")
    print(content)

#Writefile
# file_path = "C:/code/crypto/cryptoProject/cryptoProject/text.txt"
# content_to_write = b""
# writeFile(content_to_write, file_path)
# print("ไฟล์ถูกเขียนเรียบร้อยแล้ว")

