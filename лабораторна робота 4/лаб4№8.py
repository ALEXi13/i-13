# *-* coding: utf-8 *-*
# Меню
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
    X=input(">>> Введіть номер пункту меню")
    if X==1:
        a=input('Введіть початок діапазону')
        b=input('Введіть кінець діапазону')
        x=0
        for x in range(a,b):
            x+=1
            if x%7==0:
                print x
    if X==2:
        n = input('Кількість елементів в мережі')
        s = 0 #suma
        for i in range(n):
            a=input('opir')
            i+= 1
            s=a+i
    print s
    if X==3:
        suma=0
        for x in range(1,6):
            k=0
            while k<141:
                x=k
                for i in range(1,k):
                    suma+=((-1**k)*(x**k))*(1.0/k*3.0+k*((x+1)**1.0/2))
                    k+=1
        print 'suma',suma
    if X==4:
        i=10
        while i>0:
            print i,"green bottles hanging on the wall,"
            print i,"green bottles hanging on the wall,"
            print "And if one green bottle should accidentally fall,"
            i-=1
            print "There’ll be", i, "green bottles hanging on the wall."
    if X==5:
        zerna=input("Введите вагу одного зерна")
        zerna2=zerna
        suma1=0
        for i in range(64):
            print i+1,"=", zerna
            suma1+=zerna
            zerna*=2
        print 'suma vseh zeren',suma1
        # Второй способ, без использования цикла
        suma2=zerna2*(1-2**64)/(1-2)
        print "suma vseh zeren", suma2
    if X==6:
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
    if X==7:
        def Primes(N):
            primes = [i for i in range(1,N+1)]
            primes[0] = 0
            for i in xrange(0, N):
                if primes[i] != 0:
                    for j in xrange(i+primes[i],N,primes[i]):
                        primes[j] = 0
            return [x for x in primes if x != 0]
        print Primes(102)
    else:
        print"Оберіть пункт від 1 до 8"
    continue