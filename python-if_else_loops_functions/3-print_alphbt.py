#!/usr/bin/python3
for bet in range(97, 123):
    if chr(bet) not in ['q', 'e']:
        print("{}".format(chr(bet)), end='')
