# CSC382
# Matthew Connelly
# Project 1
# 2/2/20

# file: fibtest.py - timing fibonacci functions defined in fib.py

from fib import *
import time
import random

# fib computation times
fibTime, fibRTime = 0,0

# for print msg formatting
msgWidth = 5 

# printed table header
print('int',' '*msgWidth, 'fib',' '*msgWidth, 'fibR',' '*msgWidth, 'val')

# generate 16 random fib numbers
for i in range(17):

	# random number
	n = random.randint(1,35)

	# store nth fib
	val = fib(n)

	# nonrecursive fib time
	now = time.time()
	fib(n)
	fibTime = time.time() - now

	# recursive fib time
	now = time.time()
	fibR(n)
	fibRTime = time.time() - now

	# print results
	print(n,' '*msgWidth,round(fibTime,4),' '*msgWidth, round(fibRTime,4),' '*msgWidth, val)
