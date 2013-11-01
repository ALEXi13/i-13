#-*-coding:utf-8-*-
#Volodin Misha
#max_n = максимум чисел
#massive = масив с числами
#fn = число с которого начинаеться проверка (first number)
#a = переменная умножения простого числа
#massive2 = Новый масив с простыми числами

max_n = 100
massive = [0] * max_n
for x in range(max_n):
    massive[x] = x

massive[1] = 0

fn = 2
while fn < max_n:
    if massive[fn] != 0:

        a = fn * 2
        while a < max_n:
            massive[a] = 0
            a = a + fn
    fn += 1

massive2 = []
for x in massive:
    if massive[x] != 0:
        massive2.append(massive[x])
del massive
print (massive2)
