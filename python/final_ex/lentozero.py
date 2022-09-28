# ID 70942661
from typing import List


def lentozero(n: int, numbers: List[str], reverse: List[str]) -> str:
    count = n
    result = []
    reverse_res = []
    for i in range(n):
        if numbers[i] == '0':
            count = 0
            result.append(0)
        else:
            count += 1
            result.append(count)

    for i in range(n):
        if reverse[i] == '0':
            count = 0
            reverse_res.append(0)
        else:
            count += 1
            reverse_res.append(count)
    y = reversed(tuple(reverse_res))

    print(*map(min, zip(result, y)))


def read_input():
    n = int(input())
    numbers = input().split()
    reverse = list(reversed(numbers))
    return n, numbers, reverse


n, numbers, reverse = read_input()
lentozero(n, numbers, reverse)
