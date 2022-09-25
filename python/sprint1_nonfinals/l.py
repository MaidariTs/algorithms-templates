from typing import Tuple


def get_excessive_letter(shorter: str, longer: str) -> str:
    li = []
    a = sorted(list(shorter))
    b = sorted(list(longer))
    print(a)
    print(b)
    if a[0] != b[0]:
        x = a[::-1]
        x.append('0')
        a = x[::-1]
    else:
        a.append('0')
    for i in range(len(b)):
        if a[i] != b[i]:
            li.append(b[i])
    return li


def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer


shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
