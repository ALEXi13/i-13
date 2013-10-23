# *-* coding: utf-8 *-*
import sys
import time
s=u"\u2665"
s2=u"\u263a"
for x in range(101):
    sys.stdout.flush()
    sys.stdout.write('\rProgress: %3s %% %3s%3s' % (x,s*x,s2*(101-x)))
    time.sleep(0.1)