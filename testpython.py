import math

item = 10399

def main():
    bit_len = math.ceil(item.bit_length() / 8)
    c = item.to_bytes(bit_len, byteorder='big')  # Use 'big' byte order
    print("c (hex) ", c.hex().upper())

main()