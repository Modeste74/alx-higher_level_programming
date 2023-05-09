#!/usr/bin/python3
def uppercase(str):
    convert = ""
    for lower in str:
        if 97 <= ord(lower) <= 122:
            convert += chr(ord(lower) - 32)
        else:
            convert += lower
    print("{:s}".format(convert))
