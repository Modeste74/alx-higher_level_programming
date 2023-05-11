#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    num_arg = len(args)
    if num_arg == 0:
        print("No arguments.")
    elif num_arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_arg))
    for i, arg in enumerate(args):
        print("{}: {}".format(i + 1, arg))
