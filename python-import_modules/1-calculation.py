#!/usr/bin/python3
from calculator_1 import add, sub, div, mul


a = 10
b = 5


if __name__ == "__main__":

    result = add(a, b)
    print("{} + {} = {}".format(a, b, results))

    result = sub(a, b)
    print("{} - {} = {}".format(a, b, results))

    result = div(a, b)
    print("{} / {} = {}".format(a, b, results))

    result = mul(a, b)
    print("{} * {} = {}".format(a, b, results))
