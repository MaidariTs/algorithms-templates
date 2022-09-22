from typing import List, Tuple


def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    len_matrix_row = len(matrix) - 1
    len_matrix_col = len(matrix[0]) - 1
    x = matrix[row][col]
    list = []
    # Добавить условие на кол-во столбцов и строк

    if x == matrix[0][0]:
        list.append(matrix[row][col+1])
        list.append(matrix[row+1][col])
        return sorted(list)

    elif x == matrix[row][0]:
        list.append(matrix[row][col+1])
        list.append(matrix[row-1][col])
        list.append(matrix[row+1][col])
        return sorted(list)

    elif x == matrix[0][len_matrix_col]:
        list.append(matrix[row][col-1])
        list.append(matrix[row+1][col])
        return sorted(list)

    elif x == matrix[len_matrix_row][0]:
        list.append(matrix[row][col+1])
        list.append(matrix[row-1][col])
        return sorted(list)

    elif x == matrix[len_matrix_row][len_matrix_col]:
        list.append(matrix[row][col-1])
        list.append(matrix[row-1][col])
        return sorted(list)

    elif x == matrix[row][len_matrix_col] and (
         x != matrix[0][len_matrix_col] or
         x != matrix[len_matrix_row][len_matrix_col]):
        list.append(matrix[row][col-1])
        list.append(matrix[row-1][col])
        list.append(matrix[row+1][col])
        return sorted(list)

    elif x == matrix[0][col] and (
         x != matrix[0][0] or x != matrix[0][len_matrix_col]):
        list.append(matrix[row][col-1])
        list.append(matrix[row][col+1])
        list.append(matrix[row+1][col])
        return sorted(list)

    elif x == matrix[len_matrix_row][col]:
        list.append(matrix[row][col-1])
        list.append(matrix[row][col+1])
        list.append(matrix[row-1][col])
        return sorted(list)

    else:
        list.append(matrix[row][col-1])
        list.append(matrix[row][col+1])
        list.append(matrix[row-1][col])
        list.append(matrix[row+1][col])
        return sorted(list)


def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col


matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
