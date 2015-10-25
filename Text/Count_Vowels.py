# -*- coding: utf-8 -*-
__author__ = 'Delbert'


"""
Count Vowels - Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.
"""

def Count(s):
    cnt = {
        "a":0,
        "e":0,
        "i":0,
        "o":0,
        "u":0
    }

    for letter in s:
        if letter in "aeiou":
            cnt[letter] += 1

    print("Summary:")
    for v in cnt:
        print("{letter}:\t{cnt}".format(letter=v, cnt=cnt[v]))


def main():
    inp = input("String to count vowels:\t")
    Count(inp.lower())


if __name__ == "__main__":
    main()