#--coding: utf-8 --
def f():
    numbers = []
    i = 1
    while True:
        number = int(input("Введите, i, число: "))
        i += 1
        if (number == 0):
            break
        numbers.append(number)
    maximum = 0
    sec_max = 0
    sec_num = None
    for number in numbers:
        if (sec_num == number):
            maximum += 1
        else:
            if (sec_max < maximum):
                sec_max = maximum
            maximum = 0
        sec_num = number
    print(f"Максимальная последовательность одинаковых чисел:: {sec_max}")
f()
