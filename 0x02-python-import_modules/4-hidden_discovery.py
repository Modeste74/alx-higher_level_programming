#!/usr/bin/python3
import hidden_4
names = dir(hidden_4)
for name in sorted(names):
    if name[:2] != "__":
        print("{:s}".format(name))
