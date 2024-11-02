#!/usr/bin/env python3

def validUTF8(data):
    # Number of bytes expected for the current character
    num_bytes_expected = 0

    for num in data:
        # Get the byte value (the least significant 8 bits)
        byte = num & 0xFF
        
        # Determine the number of bytes for the character
        if num_bytes_expected == 0:
            if (byte & 0x80) == 0:  # 1-byte character
                continue
            elif (byte & 0xE0) == 0xC0:  # 2-byte character
                num_bytes_expected = 1
            elif (byte & 0xF0) == 0xE0:  # 3-byte character
                num_bytes_expected = 2
            elif (byte & 0xF8) == 0xF0:  # 4-byte character
                num_bytes_expected = 3
            else:
                return False  # Invalid start byte
        else:
            # Checking continuation bytes
            if (byte & 0xC0) != 0x80:  # Valid continuation byte starts with '10'
                return False
            num_bytes_expected -= 1
    
    # If we are not expecting any more bytes at the end, it's valid
    return num_bytes_expected == 0

