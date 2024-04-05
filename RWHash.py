import math
import padding
import cryptoMath

def RWHash(msg, p):
    pLen = p.bit_length()-1
    compress = compression(msg,p,pLen)
    pad_compress = padding.pad_with_ones(bin(compress)[2:],pLen)
    return int(pad_compress,2)

def compression(msg,p, pLen):
    print("plen ", pLen)
    size = (pLen*5)
    # blocks = block_split(msg, size)
    # print("Blocking ", blocks)
    h0 = len(msg)
    # print("h0 ", h0)
    hash = 0
    for i in range(0, len(msg), pLen) :
        block = msg[i:i+size]
        if(len(block)<size):
            block = padding.pad_with_ones(block,size)
        # print("block i ", i, " = ", block)
        split = block_split(block, pLen)
        c1 = sumChunk(split,p)
        # print("c1 ", c1)
        hash = h0+c1
        # print("hash = ", bin(hash)[2:])
        hash_shift = rightRotate(bin(hash)[2:]) % p
        # print("shift hash = ", hash_shift)
        h0 = hash_shift
        # print("c1 = ", c1 ,"hash = ",hash)
        # shift right 16 bits
    return hash_shift

def blocking(msg, s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the binary string in steps of 4 bits
    for i in range(0, len(msg), s):
        # Extract a substring of 4 bits
        substring = msg[i:i+s]
        # Append the substring to the list
        substrings.append(substring)

    return substrings

def sumChunk(comSplit, p):
    sum = 0 

    count = 1
    
    for chunk in comSplit:
        sum += cryptoMath.mod_exp(int(chunk,2), count, p)
        count += 1
    
    return sum

def block_split(text, block_size):

    blocks = []
    padlen = 0
    for i in range(0, len(text), block_size):
        bi = text[i:i+block_size]
        # blocks.append(bin)
        # print("len ", len(text), " idx : ", i)
        if(len(bi)==block_size):
            blocks.append(bi)
        else:
            pad = padding.pad_with_ones(bi, block_size)
            # print("blocking pad ",pad)
            blocks.append(pad)
    # print("block split to ", blocks)
    return blocks

def rightRotate(n, shift_size=16):
    lst = binary_to_list(n)
    # print("list of binary ", lst)
    shift_size = shift_size % len(lst)
    shifted = lst[-shift_size:] + lst[:-shift_size]
    binary = ''.join(str(bit) for bit in shifted)
    # print("shifted ", binary)
    return int(binary,2)

def binary_to_list(binary_str):
    return [int(bit) for bit in binary_str]

print(RWHash("11010101011111000010101010", 17))