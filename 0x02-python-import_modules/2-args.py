#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv[1:]
    num_arg = len(arg)
    if num_arg == 0:
        print("No argument.")
    elif num_arg == 1:
        print("1 argument:")
    else:
        print("{} argument:".format(num_arg))
    for i in range(num_arg):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
