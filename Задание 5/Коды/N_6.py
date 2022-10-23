#--coding: utf-8 --
def f():
    numbers = []
    i = 1
    while True:
        num = None
        try:
            num = int(input(f"Введите {i} неотрицательно число: "))

            if (num >= 0):
                i += 1
                if (num != 0):
                    numbers.append(num)
                else:
                    break
            else:
                print("Вы ввели неправильное число")
        except ValueError:
            print("Вы ввели неправильное число")
    amount = 0
    for num in numbers:
        amount += num
    result = amount/len(numbers)
    print(f"Среднее значение элементов в массиве равно: {result}")
f()
