#!/usr/bin/python3
def no_c(my_string):
    new_s = ""
    char = 'c'
    char1 = 'C'
    for i in my_string:
        if i != char and i != char1:
            new_s += i
    return new_s
