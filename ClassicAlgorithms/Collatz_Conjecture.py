# -*- coding: utf-8 -*-
__author__ = 'Delbert'

"""
Start with a number n > 1. Find the number of steps it takes to reach one using the following process: If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
"""

def ColCon(num, cnt=0):
    cnt += 1
    print("{count}:\t{num}".format(count=cnt, num=num))
    if num == 1:
        print("It takes {cnt} steps to reach 1.".format(cnt=cnt))
    elif num%2:
        num = 3*num + 1
        ColCon(num, cnt)
    else:
        num = int(num/2)
        ColCon(num, cnt)



def main():
    num = int(input("Enter a number:\t"))
    ColCon(num)


if __name__ == "__main__":
    main()