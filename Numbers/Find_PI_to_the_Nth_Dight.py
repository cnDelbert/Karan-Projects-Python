# -*- coding: utf-8 -*-
# __author__ == 'Delbert'


import math


def nth_digit(n):
    if int(str(n)) > 48:
        print('Sorry, the number %s is too large.' % n)
        return
    print('%.*f' % (int(str(n)), math.pi))


def main_loop():
    while True:
        n = input("Please input a digit:")
        if str(n).isdigit():
            nth_digit(int(n))
        elif n == 'quit':
            break
        else:
            print('Error, %s is not a number.' % n)


if __name__ == '__main__':
    main_loop()