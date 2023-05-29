#!/usr/bin/python3
def safe_print_integer(value):
    try:
        try:
            print("{:d}".format(value))
        except ValueError:
            raise
        return True
    except Exception:
        return False
