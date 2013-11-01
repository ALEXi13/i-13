# *-* coding: utf-8 *-*
# Меню програми

while True:
    print ">>> Головне меню"
    print "Завдання 1: Вивести всы числа крані 7, в заданому діапазоні"
    print "Завдання 2: Знайти загальний опір"
    print "Завдання 3: Обчислити суму"
    print "Завдання 4: Текст пісні"
    print "Завдання 5: Задача про зерна"
    print "Завдання 6: Індикатор виконання"
    print "Завдання 7: Вивести прості числа"
    print "Завдання 8 ви спостерігаєте зараз", u"\u263a"
    punkt=input(">>> Введіть номер пункту меню")
    if punkt==1:
        from math import pi
        for i in range(1,11):
            grad=int(i*180/pi)
            min=int(((i*180/pi)-(i*180//pi))*60)
            s=u'\u00b0'
            print i, "rad =",grad, s, min,"'"
    if X==2:
        N=input("Введите количество чисел")
        sum=0
        for i in range(N):
            chislo=input("Введите число")
            sum+=chislo
        else:
            print "Среднее арифметическое =", round(1.0*sum/N,3)
    if X==3:
        from math import factorial
        sum=0
        for x in range(1,6):
            for k in range(171):
                sum+=(-1)**k*1.0*(k+1)*x**k/factorial(k)
        print "Сумма =", sum
    if X==4:
        i=10
        while i>0:
            print i,"green bottles hanging on the wall,"
            print i,"green bottles hanging on the wall,"
            print "And if one green bottle should accidentally fall,"
            i-=1
            print "There’ll be", i, "green bottles hanging on the wall."
    if X==5:
        zena=input("Введите цену одного зерна")
        zena2=zena
        suma1=0
        for i in range(64):
            print i+1,"=", zena
            suma1+=zena
            zena*=2
        print "Сумма, полученная с помощью цикла",suma1

        # Второй способ, без использования цикла
        suma2=zena2*(1-2**64)/(1-2)
        print "Сумма,  использованием геометрической прогресии", suma2
    if X==6:
        import sys
        import time
        s=u"\u2665"
        s2=u"\u263a"
        for x in range(101):
            sys.stdout.flush()
            sys.stdout.write('\rProgress: %3s %% %3s%3s' % (x,s*x,s2*(100-x)))
            time.sleep(0.1)
    if X==7:
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
    if X==8:
        break
    else:
        print"Оберіть пункт від 1 до 8"
        continue
