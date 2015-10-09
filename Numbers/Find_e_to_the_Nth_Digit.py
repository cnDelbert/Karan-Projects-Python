# -*- coding: utf-8 -*-
# __author = 'Delbert'

import math


def nth_digit():
	while True:
		n = input('Please input a number: ')
		if n == 'quit':
			return
		elif n.isdigit():
			if int(n) > 48:
				print('Sorry, the number you input is too large.')
			else:
				print('%.*f' % (int(n), math.e))
		else:
			print('Error, %s is not an integer. Please retry.')


if __name__ == '__main__':
	nth_digit()