# *-* coding: utf-8-*-*
# Лабораторна 4 завдання 5(1 спосіб)
zerna=input("Введите вагу одного зерна")
zerna2=zerna
suma1=0
for i in range(64):
    print i+1,"=", zerna
    suma1+=zerna
    zerna*=2
print 'suma vseh zeren',suma1