#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if idx < 0 or idx > length:
        return my_list
    new = []
    for n in range(length):
        if n != idx:
            new.append(my_list[n])
    my_list [:]= new
    return my_list
