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
        if self.size != self.max_n:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            return 'error'

    def push_front(self, value):
        if self.size != self.max_n - 1:
            self.queue[self.head] = value
            self.head = (self.head + 1) % self.max_n
            self.tail = (self.tail + 1) % self.max_n
            self.queue[self.tail] = value
            self.size += 1
        else:
            return 'error'

    def pop_front(self, value):
        pass
    def pop_back(self, value):
        pass


# n - количество команд
# m - максимальный размер дека
n = int(input())
m = int(input())
deq = 
# res = []
# for i in range(n):
#     command = input().split()
#     if len(command) == 2:
#         a = s.put(command[1])
#         if a == 'error':
#             res.append(a)
#     if command[0] == 'get':
#         res.append(s.get())
#     if command[0] == 'size':
#         res.append(s.size)

# for x in res:
#     print(x)
    