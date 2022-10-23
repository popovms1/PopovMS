#--coding: utf-8 --
def f():
    numbers = []
    i = 1

    while True:
        number = int(input("Введите, i, число: "))

        i += 1
        if (number != 0):
            numbers.append(number)
        else:
            break


    sec_number = numbers[0]
    j = 0
    for number in numbers:
        if (sec_number < number):
            j += 1

    print(f"Число чисел больших чем предыдущее:", j)
f()