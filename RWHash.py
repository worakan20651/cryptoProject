import math
import padding

def RWHash(msg, size, p):
    pass

def compression(msg):
    
    pass

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

def sumChunk(blockingValue, size, p):
    sum = 0 
    
    h0 = size%p
    
    for chunk in blockingValue:
        
    