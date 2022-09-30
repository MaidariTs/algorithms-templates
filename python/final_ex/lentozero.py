# ID 71029123
from typing import List


def lentozero(n: int, numbers: List[str], reverse: List[str]) -> str:
    count = n
    result = [None] * n

    for i in range(n):
        if numbers[i] == '0':
            count = 0
            result[i] = 0
        else:
            count += 1
            result[i] = count

    for i in range(n):
        if reverse[i] == '0':
            count = 0
            reverse[i] = 0
        else:
            count += 1
            reverse[i] = count

    y = reverse[::-1]
    final = " ".join(map(str, list(map(min, tuple(zip(result, y))))))
    return final


def read_input():
    n = int(input())
    numbers = input().split()
    reverse = list(reversed(numbers))
    return n, numbers, reverse


if __name__ == '__main__':
    n, numbers, reverse = read_input()
    print(lentozero(n, numbers, reverse))
