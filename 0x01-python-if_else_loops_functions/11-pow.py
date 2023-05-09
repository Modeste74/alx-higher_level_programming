#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b == 0:
        return 1
    elif b > 0:
        for n in range(b):
            result *= a
    else:
        for n in range(abs(b)):
            result *= 1/a
    return result
