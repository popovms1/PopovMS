def f():
    N = int(input("Введите натуральное число: "))
    if (N >= 1):

        i = 0
        twoinpower = 1

        while (twoinpower < N):
            twoinpower *= 2
            i += 1

        if (twoinpower > N):
            i -= 1
            twoinpower = 1

            for _ in range(1, i+1):
                twoinpower *= 2

        print(f'Самое больше число 2 в степени: {twoinpower}')
        print(f'Самая большая степень: {i}')
f()