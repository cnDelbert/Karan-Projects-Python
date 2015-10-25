# -*- coding: utf-8 -*-
__author__ = 'Delbert'

"""
Check if Palindrome - Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”
"""


def Palindrome(s):
    for i in range(len(s)//2):
        if s[i] == s[-(i+1)]:
            continue
        else:
            return False
    return True

def main():
    print("Welcome to Check if Palindrome")
    while True:
        inp = input("A word is needed:\t")
        if not inp or " " in inp:
            print("Error: A word is needed!")
            continue
        elif "EXIT" == inp:
            break
        else:
            if Palindrome(inp.lower()):
                print("Yes, %s is a palindrome." % inp)
            else:
                print("No, %s is not a palindrome." % inp)

if __name__ == "__main__":
    main()