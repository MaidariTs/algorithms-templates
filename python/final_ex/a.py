import re

# abs(x) - модуль числа x
# min(str, int, key=len)

def lentozero(n: str) -> str:
    lis = []
    
    result = ''
    n = re.sub(', ', '', n)
    len_n = len(n)
    for i in range(len_n):
        if n[i] == '0':
            lis.append(i)
    index_zero = lis
    print(index_zero)
     
    ГЛЯНУТЬ В TEST.PY

    for i in range(len_n):
        if n[i] == '0':
            result += '0'
        else:
            if i - 
            for p in range(len(index_zero)):
                asd = i - index_zero[p]
                result += str(abs(asd))
    return result


print(lentozero('0, 1, 1, 1, 0'))


# first = []
#     two = []
#     result = ''
#     n = re.sub(', ', '', n)
#     n_reversed = n[::-1]
#     len_n = len(n)
#     print(n)
#     print(n_reversed)
#     for i in range(len_n):
#         if n[i] == '0':
#             result += '0'
#         elif n[i] != '0':
            

    # for i in range(len_n):
    #     for p in range(len(index_zero)):
    #         index_zero.append['1']
    #         if str(abs(i - index_zero)) <= str(abs(i - index_zero[p+1])):
    #             result += (str(abs(i - index_zero[p])))
    # return result
    
