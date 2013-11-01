#-*-coding:utf-8-*-
import time
while True:
    print ""
    print " +-------------------Головне меню-------------------+"
    print " | [1]Квадрати всіх цілих чисел від а до b          |"
    print " | [2]Сума косинусів чисел                          |"
    print " | [3]Обчислення факторіалу                         |"
    print " | [4]Текст пісні 'Ten Green Bottles'               |"
    print " | [5]Визначення ваги зерен за легендою (З циклом)  |"
    print " | [6]Визначення ваги зерен за легендою (Без циклу) |"
    print " | [7]Progress bar                                  |"
    print " | [8]Знаходження простих чисел від 2 до 100        |"
    print " | [0]Вихід з меню                                  |"
    print " +--------------------------------------------------+"

    run=input("Введіть номер програми")
    if run==1:
        run1=open("Lab4_1.py")
        exec(run1)
        time.sleep(3)
    elif run==2:
        run2=open('Lab4_2.py')
        exec(run2)
        time.sleep(3)
    elif run==3:
        run3=open('Lab4_3.py')
        exec(run3)
        time.sleep(3)
    elif run==4:
        run4=open('Lab4_4.py')
        exec(run4)
        time.sleep(3)
    elif run==5:
        run5=open('Lab4_5.py')
        exec(run5)
        time.sleep(3)
    elif run==6:
        run6=open('Lab4_5_2.py')
        exec(run6)
        time.sleep(3)
    elif run==7:
        run7=open('Lab4_6.py')
        exec(run7)
        time.sleep(3)
    elif run==8:
        run8=open('Lab4_7.py')
        exec(run8)
        time.sleep(3)
    elif run==0:
        break
    else:
        print ("Некоректна дія")

