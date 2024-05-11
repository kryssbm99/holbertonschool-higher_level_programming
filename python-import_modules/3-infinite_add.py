#!/usr/bin/python3
import sys


def sum_arguments(args):
    total = sum(int(arg) for arg in args)
    return total


if __name__ == "__main__":
    args = sys.argv[1:]

    if args:
        result = sum_arguments(args)
        print(result)
    else:
        print(0)
