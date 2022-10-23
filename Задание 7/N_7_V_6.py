#--coding: utf-8 --
def f():
    mas = []
    more = 0

    for _ in range(10):
        _ = int(input("Enter element of massive: "))
        mas.append(_)

    for _ in mas:
        if (_ > 5):
            more += 1

    print(f"Elements greater than 5 is: {more}")
f()
