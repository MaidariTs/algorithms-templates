# ID 71031750
def sleight_of_hand(k: int, matrix: str) -> int:
    k = k*2
    dict_count = {}
    count = 0
    for i in matrix:
        if i in dict_count:
            dict_count[i] += 1
        else:
            dict_count[i] = 1
    val = list(dict_count.values())
    for i in range(len(val)):
        if val[i] <= k:
            count += 1
    return count


def read_input():
    k = int(input())
    m = ''
    for i in range(4):
        m += input()
    matrix = m.replace('.', '')
    return k, matrix


if __name__ == '__main__':
    k, matrix = read_input()
    print(sleight_of_hand(k, matrix))
