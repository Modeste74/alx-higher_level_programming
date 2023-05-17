#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_num = set()
    sum_uniq = 0
    for n in my_list:
        if n not in uniq_num:
            uniq_num.add(n)
            sum_uniq += n
    return sum_uniq
