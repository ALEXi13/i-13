# *-* coding: utf-8 *-*
# Перевод из радиан в градусы

from math import pi
print "rad=grad min"
for i in range(1,10):
    grad=int(i*180/pi)
    min=int(((i*180/pi)-(i*180//pi))*60)
    print i,"=",grad, min