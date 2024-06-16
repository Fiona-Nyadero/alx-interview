#!/usr/bin/python3
'''Module looks for valid UTF-8 encoding data'''


def validUTF8(data):
    '''Returns True if UTF-8 encoding is valid'''
    bytes_checker = 0

    for n in data:
        if bytes_checker == 0:
            if (n >> 3) == 0b11110:
                bytes_checker = 3
            elif (n >> 4) == 0b1110:
                bytes_checker = 2
            elif (n >> 5) == 0b110:
                bytes_checker = 1
            elif (n >> 7) & 1:
                return False
        else:
            if (n >> 6) != 0b10:
                return False
            bytes_checker -= 1

    return bytes_checker == 0
