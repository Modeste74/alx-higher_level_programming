#!/usr/bin/python3
def uppercase(str):
    for lower in str:
        if 97 <= ord(lower) <= 122:
            lower =  chr(ord(lower) - 32)
        print(lower, end='')
    print()
