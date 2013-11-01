# -*-coding: utf-8 -*-
A=input ('Vvedite dlinny indikatora ')
B=input ('Procent zapolneniya ')
C=A/100.0*B
G=A-C
import sys
import time
for x in range(101):
    sys.stdout.flush()
    sys.stdout.write('\rProgress: %3s %%' % x)
    time.sleep(0.1)
    D=u'\u2593'
    F=u'\u2345'
print int(C)*D+int(G)*F