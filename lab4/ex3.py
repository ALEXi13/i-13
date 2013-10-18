# -*- coding: utf-8 -*-
#comment
import sys

suma = 0
for x in xrange(1, 6):
    print x
    k = 0
    while k < 5000:
        if k == 0:
            k += 1
            continue
        fk=k
        for i in range(1,k):
            fk *= i
        suma += ((-1)**(k+1)*x**(2*k+1))/(fk*(2*k+1))
        k +=1
        sys.stdout.flush()
        sys.stdout.write('\r Progress: %s %%' % str(k/50.0))
print suma
