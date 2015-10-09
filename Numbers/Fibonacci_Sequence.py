# coding:utf-6
# __author__ = 'Delbert'

def FibSeq(n):
	if n == 1 or n == 2:
		return 1
	else:
		return 1 + FibSeq(n-1)


def main():
	while True:
		n = input('Please input a number:')
		if n == 'quit':
			return
		elif n.isdigit() and int(n) > 0:
			print(FibSeq(int(n)))
		else:
			print("Error, a number is needed.")


if __name__ == '__main__':
	main()