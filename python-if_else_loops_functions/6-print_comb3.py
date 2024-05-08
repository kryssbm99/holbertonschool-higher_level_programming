#!/usr/bin/python3
for tens in range(0, 9):
    for ones in range(tens + 1, 10):
        if tens != 8 or ones != 9:
            print("{:d}{:d}".format(tens, ones), end=', ')
        else:
            print("{:d}{:d}".format(tens, ones), end='\n')
