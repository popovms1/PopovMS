def main_func(fraction_1, fraction_2):
    fraction_2 = fraction_2[::-1]
    nod = gcd(fraction_1[1], fraction_2[1])
    return f"{int((fraction_1[0]/nod) * (fraction_2[0]/nod))}/{int(fraction_1[1]/nod * fraction_2[1]/nod)}"


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


fraction_1 = list(map(int, input("A/B: ").split("/")))
fraction_2 = list(map(int, input("C/D: ").split("/")))

print(main_func(fraction_1, fraction_2))
