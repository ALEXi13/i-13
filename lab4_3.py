#-*-coding:utf-8-*-
#volodin misha

import sys

summ=0
for x in range(1,6):
    k=0
    while k<10000:
        if k==0:
            k+=1
            continue
        fk=k
        for i in range(1,k):
            fk*=i
        summ+=((-1**k)*((x/2)**(2*k+1)))/((k+1)*fk)
        k+=1
        sys.stdout.flush()
        sys.stdout.write('\r Progress: %s %%' % str(k/50.0))
print ("сумма="), summ
