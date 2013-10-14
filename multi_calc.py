#!/usr/bin/python

import sys


def mult(first, second):
	if (first > 10) or (second > 10):
		print 'digit greater than 10 has been entered. CANNOT COMPUTE BRO'
	else:
		total = first * second
		return total


def main():
	print 'Welcome to the Multiplcation-only Calculator!'
	print 'My name is not Nathan. It\'s Nathaniel BRO!'

	a = int(raw_input('Please enter your first number '))
	b = int(raw_input('Please enter your second number '))

	print mult(a, b)




# run main when called
if __name__ == "__main__":
	main()
