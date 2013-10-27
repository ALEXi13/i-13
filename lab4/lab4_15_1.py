# *-* coding: utf-8 *-*
# Из радиан в градусы


from math import pi
for i in range(1,11):
    grad=int(i*180/pi)
    min=int(((i*180/pi)-(i*180//pi))*60)
    s=u'\u00b0'
    print i, "rad =",grad, s, min,"'"