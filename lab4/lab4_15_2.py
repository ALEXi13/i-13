# *-* coding: utf-8 *-*
# Среднее арифметическое чисел

N=input("Введите количество чисел")
sum=0
for i in range(N):
    chislo=input("Введите число")
    sum+=chislo
else:
    print "Среднее арифметическое =", round(1.0*sum/N,3)