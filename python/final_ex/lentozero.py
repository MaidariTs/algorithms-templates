# ID 71054567
from typing import List
import sys


def lentozero(n: int, numbers: List[str]) -> str:
    count = n

    for i in range(n):
        if numbers[i] == '0':
            count = 0
            numbers[i] = 0
        else:
            count += 1
            numbers[i] = count
    return numbers


def read_input():
    n = int(sys.stdin.readline())
    numbers = sys.stdin.readline().split()
    rev_num = numbers[::-1]
    return n, numbers, rev_num


if __name__ == '__main__':
    n, numbers, rev_num = read_input()
    merged_list = tuple(zip(
        lentozero(n, numbers), reversed(
            lentozero(n, rev_num))))
    print(" ".join(map(str, list(map(min, merged_list)))))
