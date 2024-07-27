#!/usr/bin/python3
'''Module looks for valid UTF-8 encoding data'''


def validUTF8(data):
    '''Returns True if UTF-8 encoding is valid'''
    def is_start_byte(byte):
        return (byte & 128) == 0 or (byte & 224) == 192 or \
               (byte & 240) == 224 or (byte & 248) == 240

    def is_continuation_byte(byte):
        return (byte & 192) == 128

    bytes_checker = 0
    for n in data:
        if bytes_checker == 0:
            if not is_start_byte(n):
                return False
            if (n & 224) == 192:
                bytes_checker = 1
            elif (n & 240) == 224:
                bytes_checker = 2
            elif (n & 248) == 240:
                bytes_checker = 3
        else:
            if not is_continuation_byte(n):
                return False
            bytes_checker -= 1
    return bytes_checker == 0
