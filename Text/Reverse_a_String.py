# -*- coding: utf-8 -*-
__author__ = 'Delbert'

"""Reverse a String - Enter a string and the program will reverse it and print it out."""


def reverse(s):
    return s[::-1]


def main():
    while True:
        inp = input("Input a string:\t")
        if inp == "EXIT":
            break
        elif not inp:
            continue
        else:
            print(reverse(inp))


if __name__ == "__main__":
    main()