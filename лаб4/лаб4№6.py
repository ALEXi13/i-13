# *-* coding: utf-8-*-*
# Лабораторна 4 завдання 6
dlina=input ('Vvedite dlinny indikatora ')
proc=input ('Procent zapolneniya ')
import sys
import time
s=u"\u2665"
s2=u"\u263a"
for x in range(dlina):
    sys.stdout.flush()
    sys.stdout.write('\rProgress: %3s %% %3s%3s' % (x,s*x,s2*(100-x)))
    time.sleep(0.1)



