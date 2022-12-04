def task(a, b, r, c):
    print(len(list(filter(lambda z: (z[0] - a)**2 + (z[1] - b)**2 < r**2, c))))


P = list(map(int, input("P: ").split()))
F = list(map(int, input("F: ").split()))
L = list(map(int, input("L: ").split()))

A = int(input("A: "))
B = int(input("B: "))
R = int(input("R: "))

task(A, B, R, [P, F, L])
