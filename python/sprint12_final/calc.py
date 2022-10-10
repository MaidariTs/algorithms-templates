# 71742783
from typing import List


class Stack:
    def __init__(self):
        self.items = []

    # def isEmpty(self):
    #     return self.items == []

    def push(self, item):
        self.items.append(int(item))

    def pop(self):
        return self.items.pop()


def read_input():
    seq = input().split()
    return seq


def calc(seq: List[str]) -> int:
    dictionary = {
        '+': lambda x, y: x+y,
        '-': lambda x, y: y-x,
        '*': lambda x, y: x*y,
        '/': lambda x, y: y//x
    }
    stack = Stack()
    for i in seq:
        try:
            stack.push(int(i))
        except Exception:
            stack.push(dictionary[i](stack.pop(), stack.pop()))
    return stack.items[len(stack.items) - 1]


if __name__ == '__main__':
    seq = read_input()
    print(calc(seq))
