def pad_with_ones(data, desired_length):
    current_length = len(data)
    if current_length >= desired_length:
        return data  # No padding needed
    
    padding_length = desired_length - current_length
    padded_data = data + '1' * padding_length
    return padded_data

def pad_with_zeros(data, block_size=8):
    
    pad_len = block_size - (len(data) % block_size)
    padding = '1' + '0' * (pad_len - 1)
    return data + padding

def unpad_zeros(padded_plaintext):
    marker_found = False
    pad_len = 0
    for i in range(len(padded_plaintext) - 1, -1, -1):
        if not marker_found and padded_plaintext[i] == '1':
            pad_len += 1  # Account for the '1' marker
            break
        elif padded_plaintext[i] == '0':
            pad_len += 1
        else:
            raise ValueError("Invalid padding marker")
    # print("count pad ", pad_len)
        
    return padded_plaintext[:-pad_len]