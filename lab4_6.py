#-*-coding:utf-8-*-
import sys
import time

a=u"\u2593"  #незаповненість
b=u"\u2592"  #заповненість

x=0

for x in range(1,101):
    c=50/100.0*x
    cint=int(c)
    total=cint*a
    unc=50-cint
    unc2=unc*b
    d=total+unc2

    sys.stdout.flush()
    sys.stdout.write(u'\rProgress: %s %s %% ' % (d,x))
    time.sleep(0.1)
    x+=1