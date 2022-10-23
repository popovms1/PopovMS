#--coding: utf-8 --
def f():
    numbers = []

    i = 1
    while True:
        num = int(input("Введите, i, не отрицательное число: "))

        if (num >= 0):
            i += 1
            if (num != 0):
                numbers.append(num)
            else:
                break
        else:
            print("Вы ввели неверное число")

    print("У вас", len(numbers), "чисел в последовательности")
f()


