# -*- coding: utf-8 _8-
__author__ = 'Delbert'

"""
Pig Latin - Pig Latin is a game of alterations played on the English language game. To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.
"""


def PigLatin(s, exclude=""):
    if not exclude:
        return s[1:] + "-" + s[0] + "ay"
    elif exclude == "qu":
        return s[2:] + "-" + s[0:2] + "ay"
    elif exclude == "vowel":
        return s + "-hay"


def main():
    print("Welcome to Pig Latin. EXIT to exit.")
    while True:
        inp = input("A word is needed:\t").lower()

        if inp == "EXIT":
            break

        if " " in inp:
            continue

        if inp.startswith("qu"):
            print(PigLatin(inp, "qu"))
        elif inp[0] in "aeiou":
            print(PigLatin(inp, "vowel"))
        else:
            print(PigLatin(inp))


if __name__ == "__main__":
    main()

"""
Pig Latin's Rule Reference:
http://blog.csdn.net/winter13292/article/details/38171395
"""
"""
(1). 元音字母是‘a’、‘e’、‘i’、‘o’、‘u’。字母‘y’在不是第一个字母的情况下，也被视作元音字母。其他字母均为辅音字母。例如，单词“yearly”有三个元音字母（分别为‘e’、‘a’和最后一个‘y’）和三个辅音字母（第一个‘y’、‘r’和‘l’）。
(2). 如果英文单词以元音字母开始，则在单词末尾加入“hay”后得到“Pig Latin”对应单词。例如，“ask”变为“askhay”，“use”变为“usehay”。
(3). 如果英文单词以‘q’字母开始，并且后面有个字母‘u’，将“qu”移动到单词末尾加入“ay”后得到“Pig Latin”对应单词。例如，“quiet”变为“ietquay”，“quay”变为“ayquay”。
(4). 如果英文单词以辅音字母开始，所有连续的辅音字母一起移动到单词末尾加入“ay”后得到“Pig Latin”对应单词。例如，“tomato”变为“omatotay”， “school” 变为“oolschay”，“you” 变为“ouyay”，“my” 变为“ymay ”，“ssssh” 变为“sssshay”。
(5). 如果英文单词中有大写字母，必须所有字母均转换为小写。 """