import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    if num_args != 1:
        print("{} arguments".format(num_args), end='')
    else:
        print("{} argument".format(num_args), end='')
    if num_args == 0:
        print(".")
    else:
        print(":")
    for count, argument in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(count, argument))
