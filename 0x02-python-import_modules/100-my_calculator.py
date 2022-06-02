#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    num_args = len(sys.argv)
    if num_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    sign = sys.argv[2]
    b = int(sys.argv[3])

    if sign is '+':
        print("{} {} {} = {}".format(a, sign, b, add(a, b)))
    elif sign is '-':
        print("{} {} {} = {}".format(a, sign, b, sub(a, b)))
    elif sign is '*':
        print("{} {} {} = {}".format(a, sign, b, mul(a, b)))
    elif sign is '/':
        print("{} {} {} = {}".format(a, sign, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
