# CSC382
# Matthew Connelly
# Project 1
# 2/2/20

# file: fib.py - fibonacci function definitions

# recursive fib
def fibR(n):
	if n == 0 or n == 1:
		return n

	if n == 2:
		return 1

	return fibR(n-1) + fibR(n-2)

# non recursive fib
def fib(n):
	if n == 0 or n == 1:
		return n

	if n == 2:
		return 1

	f1, f2 = 1, 1
	result = 0

	for i in range(3, n+1):
		result = f1 + f2
		f1 = f2
		f2 = result

	return result
