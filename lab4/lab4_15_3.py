# *-* coding: utf-8 *-*
# Сумма

from math import factorial
sum=0
for x in range(1,6):
    for k in range(171):
        sum+=(-1)**k*1.0*(k+1)*x**k/factorial(k)
print "Сумма =", sum