def pad_with_ones(data, desired_length):
    current_length = len(data)
    if current_length >= desired_length:
        return data  # No padding needed
    
    padding_length = desired_length - current_length
    padded_data = data + '1' * padding_length
    return padded_data

def pad_with_zeros(data, desired_length=8):
    current_length = len(data)
    if current_length >= desired_length:
        return data  # No padding needed
    
    padding_length = desired_length - current_length
    padded_data = '0' * padding_length + data 
    
    # print("padded ", padded_data)
    return padded_data 