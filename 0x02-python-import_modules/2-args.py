#!/usr/bin/python3
import sys
arg = sys.argv[1:]
num_arg = len(arg)
if num_arg == 0:
    print("No argument.")
elif num_arg == 1:
    print("1 argument:")
else:
    print("{} argument:".format(num_arg))


