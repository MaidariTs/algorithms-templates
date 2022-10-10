class Deque:
    def __init__(self, m):
        self.queue = [None] * m
        self.max_m = m
        self.head = 0
        self.tail = 0
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push_back(self, value):
        if self.size != self.max_m:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_m
            self.size += 1
        else:
            return 'error'

    def push_front(self, value):
        if self.size != self.max_m:
            self.queue[self.head - 1] = value
            self.head = (self.head - 1) % self.max_m
            self.size += 1
        else:
            return 'error'

    def pop_front(self):
        if self.isEmpty():
            return 'error'
        else:
            value = self.queue[self.head]
            self.queue[self.head] = None
            self.head = (self.head + 1) % self.max_m
            self.size -= 1
            return value

    def pop_back(self):
        if self.isEmpty():
            return 'error'
        else:
            value = self.queue[self.tail - 1]
            self.queue[self.tail - 1] = None
            self.tail = (self.tail - 1) % self.max_m
            self.size -= 1
            return value


def deque():
    # n - количество команд
    # m - максимальный размер дека
    n = int(input())
    m = int(input())
    deq = Deque(m)
    res = []
    for i in range(n):
        full_command = input()
        command, *args = full_command.split(' ')
        if command == 'push_back':
            a = deq.push_back(*args)
            if a == 'error':
                res.append(a)
        elif command == 'push_front':
            a = deq.push_front(*args)
            if a == 'error':
                res.append(a)
        elif command == 'pop_back':
            a = deq.pop_back()
            res.append(a)
        elif command == 'pop_front':
            a = deq.pop_front()
            res.append(a)

    for i in res:
        print(i)


if __name__ == '__main__':
    deque()
