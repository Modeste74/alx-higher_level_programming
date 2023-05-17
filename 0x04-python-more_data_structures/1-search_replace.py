#!/usr/bin/python3
def search_replace(my_list, search, replace):
    upt_list = []
    for n in my_list:
        if n == search:
            upt_list.append(replace)
        else:
            upt_list.append(n)
    return upt_list
