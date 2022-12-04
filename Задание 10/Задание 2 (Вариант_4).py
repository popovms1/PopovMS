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
with open("file.txt") as file:
    for string in file:
        matrix.append(list(map(int, string.split())))

main_func(matrix)
