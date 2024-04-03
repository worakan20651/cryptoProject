# def int_to_bin_c1(numbers):
#     byte_arrays = []
#     print("numbers to convert:", numbers)
#     binary_list = [bin(number)[2:] for number in numbers]
#     print("Binary representation:", binary_list)

#     binary_string = ''.join(binary_list)
#     print("Binary string:", binary_string)
    
#     # Convert binary string to bytes
#     byte_value = int(binary_string, 2).to_bytes((len(binary_string) + 7) // 8, 'big')
#     return byte_value

# # Example usage:
numbers = 45
# byte_value = int_to_bin_c1(numbers)
# print("Byte value:", byte_value)

print(numbers.to_bytes(2, 'big') )