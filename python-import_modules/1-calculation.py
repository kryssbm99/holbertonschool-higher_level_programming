#!/usr/bin/python3
from calculator_1 import add, sub, div, mul

a = 10
b = 5

if __name__ == "__main__":

    results = add(a, b)
    print("{} + {} = {}".format(a, b, results))

    results = sub(a, b)
    print("{} - {} = {}".format(a, b, results))

    results = div(a, b)
    print("{} / {} = {}".format(a, b, results))

    results = mul(a, b)
    print("{} * {} = {}".format(a, b, results))
