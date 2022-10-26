# 73064307
def quicksort(array):
    if len(array) <= 1:
        return array
    piv = array[len(array) // 2]
    right = []
    left = []
    mid = []
    for n in array:
        if n[1] > piv[1]:
            right.append(n)
        elif n[1] < piv[1]:
            left.append(n)
        else:
            if n[0] == piv[0]:
                mid.append(n)
            elif n[2] != piv[2]:
                right.append(n) if n[2] < piv[2] else left.append(n)
            else:
                right.append(n) if n[0] < piv[0] else left.append(n)
    return quicksort(right) + mid + quicksort(left)


def read_input():
    n = int(input())
    array = []
    for i in range(n):
        data = list(input().split())
        data[1] = int(data[1])
        data[2] = int(data[2])
        array.append(data)
    return array


def main(array):
    sort = quicksort(array)
    for s in sort:
        print(s[0])


if __name__ == '__main__':
    array = read_input()
    main(array)
