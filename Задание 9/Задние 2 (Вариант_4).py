def main_func(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < 0:
                matrix[i][j] = 0
            elif matrix[i][j] > 0:
                matrix[i][j] = 1

            if i >= j:
                print(matrix[i][j], end="\t")
        print()


matrix = []
# Ввод матрицы до пустой строки
while True:
    arr = list(map(int, input().split()))
    if arr:
        matrix.append(arr)
    else:
        break

main_func(matrix)
