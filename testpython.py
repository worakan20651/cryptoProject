def pkcs7_pad(plaintext, block_size):
    pad_len = block_size - (len(plaintext) % block_size)
    padding = bytes([pad_len] * pad_len)
    return plaintext + padding

# Example usage:
plaintext_binary = "11001101"  # Example binary representation string
block_size = 8  # Example block size (8 bits per block)

# Pad the plaintext
padded_plaintext = pkcs7_pad(plaintext_binary.encode(), block_size)

print("Padded plaintext (in binary):", padded_plaintext)