#--coding: utf-8 --
def f():
    N = int(input("Введите целое число не меньше двух: "))

    if (N >= 2):
        for i in range(2, N+1):
            if (N % i == 0):
                print("Самый меньший делитель:", i)
                break
f()