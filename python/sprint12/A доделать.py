# import numpy as np
from typing import List, Tuple


def read_input():
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    return n, m, matrix


def matrix_transposition(
                         n: int,
                         m: int,
                         matrix: Tuple[List[List[int]]]
                        ) -> str:

    # arr_matrix = np.array(matrix)
    # arr_transpose = arr_matrix.transpose()
    # i = 0
    # while i < len(arr_transpose):
    #     print(*arr_transpose[i])
    #     i += 1
    trans_matrix = [[0 for j in range(n)] for i in range(m)]
    for i in range(n):
        for j in range(m):
            trans_matrix[j][i] = matrix[i][j]
    new_list = [item for sublist in trans_matrix for item in sublist]
    for p in range(m):
        return new_list[::4]


if __name__ == '__main__':
    n, m, matrix = read_input()
    print(matrix_transposition(n, m, matrix))
