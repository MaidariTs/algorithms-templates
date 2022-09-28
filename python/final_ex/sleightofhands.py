# ID 70975632
def sleight_of_hand(k: int, matrix: str) -> int:
    k = k*2
    li = []
    count = 0
    for i in range(1, 10):
        li.append(matrix.count(str(i)))
    for p in range(9):
        if li[p] <= k and li[p] != 0:
            count += 1
    print(count)


def read_input():
    k = int(input())
    m = ''
    for i in range(4):
        m += str(input())
    matrix = m.replace('.', '')
    return k, matrix


k, matrix = read_input()
sleight_of_hand(k, matrix)
