#!/usr/bin/python3

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers where each integer represents 1 byte of data.
    :return: True if data is a valid UTF-8 encoding, else False.
    """

    def is_continuation_byte(byte):
        """Helper function to check if a byte is a continuation byte."""
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
if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))  # Output: True

    data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))  # Output: True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # Output: False
