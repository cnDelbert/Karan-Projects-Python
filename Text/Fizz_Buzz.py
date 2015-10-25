# -*- coding: utf-8 -*-
__author__ = 'Delbert'

"""
Fizz Buzz - Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.
"""


def FizzBuzz(num):
    if not num % 15:
        return "FizzBuzz"
    elif not num % 3:
        return "Fizz"
    elif not num % 5:
        return "Buzz"
    else:
        return num


def main():
    for i in range(1, 100):
        print(FizzBuzz(i))


if __name__ == "__main__":
    main()