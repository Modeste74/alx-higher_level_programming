#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                data = my_list[i]
            except IndexError:
                raise
            try:
                elements = "{:d}".format(data)
            except (ValueError, TypeError):
                continue
            print(elements, end="")
            count += 1
        print()
    except Exception as e:
        print("IndexError: list index out of range")
    return count
