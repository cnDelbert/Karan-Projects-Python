# coding: utf-8
__author__ = 'Delbert'

"""
Count Words in a String - Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.
"""

def count_by_input(inp):
    return len(inp.strip().split())


def count_by_file(inp):
    f = open(inp, "r").readlines()
    cnt = 0
    for line in f:
        cnt += len(line.strip().split())
    return cnt


def chose_mode(mode):
    if mode == "i" or mode == "input":
        inp = input("Input your string:\t")
        print(count_by_input(inp))
    elif mode == "t" or mode == "text":
        inp = input("Path to text file:\t")
        print(count_by_file(inp))


def main():
    mode = input("Which one do you want? input(i) or text(t)?")

    chose_mode(mode.lower())


if __name__ == "__main__":
    main()