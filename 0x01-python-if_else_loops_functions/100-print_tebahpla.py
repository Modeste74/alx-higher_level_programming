#!/usr/bin/python3
for i in range(ord('z'), ord('A')-1, -1):
    rev_alph = chr(i)
    case = "lower" if i%2 == 1 else "uppercase"
    print("{0} ({1}),".format(rev_alph, case), end="")
