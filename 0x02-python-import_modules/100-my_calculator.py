#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv[1:]
    length = len(args)
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    if length < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if op == '+':
            print("{} {} {} = {}".format(a, b, op, add(a, b)))
        elif op == '-':
            print("{} {} {} = {}".format(a, b, op, sub(a, b)))
        elif op == '*':
            print("{} {} {} = {}".format(a, b, op, mul(a, b)))
        elif op == '/':
            print("{} {} {} = {}".format(a, b, op, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
