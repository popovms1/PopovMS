def is_simple(n, div=None):
    if div is None:
        div = n // 2 + 1

    while div >= 2:
        if n % div == 0:
            print("NO")
            return False
        else:
            return is_simple(n, div - 1)
    else:
        print("YES")
        return True


n = int(input("N: "))
is_simple(n)
