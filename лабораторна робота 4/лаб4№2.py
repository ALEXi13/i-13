#-*-coding:utf-8-*-
#Лабораторна 4 завдання2
suma=0
for x in range(1,6):
    k=0
    while k<141:
        x=k
        for i in range(1,k):
            suma+=((-1**k)*(x**k))*(1.0/k*3.0+k*((x+1)**1.0/2))
        k+=1
print 'suma',suma