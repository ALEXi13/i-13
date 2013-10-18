# -*- coding: utf-8 -*-

suma = 0
for x in xrange(1, 6):
    k = 0
    while k < 5000:
        fk=k
        for i in range(1,k):
            fk *= i
        if fk == 0:
           fk = 1
        suma += ((-1)**(k+1)*x**(2*k+1))/(fk*(2*k+1))
        k +=1

print suma
