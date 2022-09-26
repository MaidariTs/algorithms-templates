n = int(input())
numbers = input().split()
for i in range(n):
    if numbers[i] != '0':
        ls = 10**6
        for a in range(n):
            if numbers[i - a] == '0':
                if a <= i and ls > a:
                    ls = a
                if a > i and ls > n - a:
                    ls = n - a
            numbers[i] = ls
print(*numbers)
