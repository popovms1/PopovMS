def sum_num(num, res=0):
    if not num:
        return res
    res += num % 10
    num //= 10
    return sum_num(num, res)


n = int(input("N: "))
print(sum_num(n))
