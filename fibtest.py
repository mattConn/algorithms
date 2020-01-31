from fib import *
import time
import random


fibTime, fibRTime = 0,0

# for print msg formatting
width = 5 

print('int',' '*width, 'fib',' '*width, 'fibR',' '*width, 'val')

for i in range(17):
	val = fib(i)

	n = random.randint(1,35)

	# fib time
	now = time.time()
	fib(n)
	fibTime = time.time() - now

	# fibR time
	now = time.time()
	fibR(n)
	fibRTime = time.time() - now

	print(n,' '*width,round(fibTime,4),' '*width, round(fibRTime,4),' '*width, val)
