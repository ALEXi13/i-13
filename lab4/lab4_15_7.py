# *-* coding: utf-8 *-*
# Простые числа от 2 до 100

lst=[]
lst2=[]
for i in range(2,101):
    lst.append(i)
print lst
i=2
while True:
    j=i
    a=0
    while a < len(lst):
            if (lst[a]%j)==0:
                del lst[a]
            a+=1
    if len(lst)==0:
        break
    i=lst[0]
    lst2.append(i)
print lst2

