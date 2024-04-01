def pad_with_ones(data, desired_length):
    current_length = len(data)
    if current_length >= desired_length:
        return data  # No padding needed
    
    padding_length = desired_length - current_length
    padded_data = data + '1' * padding_length
    return padded_data