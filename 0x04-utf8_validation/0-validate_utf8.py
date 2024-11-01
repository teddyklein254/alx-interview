def validUTF8(data):
    # Helper function to check if a byte is a continuation byte
    def is_continuation_byte(byte):
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        byte = data[i]
        
        # Determine the number of bytes in the current character
        if byte & 0b10000000 == 0:  # 1-byte character
            num_bytes = 1
        elif byte & 0b11100000 == 0b11000000:  # 2-byte character
            num_bytes = 2
        elif byte & 0b11110000 == 0b11100000:  # 3-byte character
            num_bytes = 3
        elif byte & 0b11111000 == 0b11110000:  # 4-byte character
            num_bytes = 4
        else:
            return False  # Invalid starting byte
        
        # Check the continuation bytes
        for j in range(1, num_bytes):
            if i + j >= len(data) or not is_continuation_byte(data[i + j]):
                return False
        
        # Move to the next character
        i += num_bytes
    
    return True

# Example usage:
data1 = [0b01001000, 0b11000010, 0b10000010]  # Valid UTF-8
data2 = [0b11000010, 0b11000010]  # Invalid UTF-8
print(validUTF8(data1))  # Output: True
print(validUTF8(data2))  # Output: False
