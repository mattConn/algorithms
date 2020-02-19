import math

rplus = (1+math.sqrt(5))/2
rminus = (1-math.sqrt(5))/2

d2 = 1/(rplus-rminus)
d1 = -d2

def f(n):
    return int(math.ceil( d1*rminus**n + d2*rplus**n ))

