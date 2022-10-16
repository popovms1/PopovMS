def f():
    a = int(input("Введите число 1: "))
    b = int(input("Введите число 2: "))
    if b > a:
        for i in range(a, b+1):
            print(i)
    else:
        for i in range (b, a+1):
            print(i)
f()