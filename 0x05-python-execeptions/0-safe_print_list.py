#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                data = my_list[i]
            except IndexError:
                break
            print(data, end="")
            count += 1
        print()
    except Exception as e:
        print("Error:", type(e).__name__)
    return count
