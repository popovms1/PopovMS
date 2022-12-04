def find_strs(matrix):
    index_min = 0
    index_max = 0
    for i in range(len(matrix)):
        if sum(matrix[i]) < sum(matrix[index_min]):
            index_min = i
        if sum(matrix[i]) > sum(matrix[index_max]):
            index_max = i
    print(f"MIN: {matrix[index_min]} | SUM: {sum(matrix[index_min])}")
    print(f"MAX: {matrix[index_max]} | SUM: {sum(matrix[index_max])}")


matrix = []
# Ввод матрицы до пустой строки
while True:
    arr = list(map(int, input().split()))
    if arr:
        matrix.append(arr)
    else:
        break

find_strs(matrix)
