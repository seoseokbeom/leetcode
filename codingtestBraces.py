import re


def solution(strn):
    cnt = 0


def recursion(strn):
    if len(strn) == 0:
        return 1
    elif strn == '()':
        return 2
    elif strn == '[]':
        return 3
    arr = []
    cnt = 0
    tmp = 0
    while len(strn):
        for i, c in enumerate(strn):
            if c == '(' or c == '[':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                arr.append(strn[:i+1])
                strn = strn[i+1:]
                break
    for seperate in arr:
        if seperate[0] == '(':
            tmp += 2*recursion(seperate[1:-1])
        elif seperate[0] == '[':
            tmp += 3*recursion(seperate[1:-1])
    return tmp


print(recursion('(()[[]])([])'))
# def solution(strn):
#     res = ''
#     for i, c in enumerate(strn):
#         if c == '(' or c == '[':
#             res += '+'
#         else:
#             print('2')
#             if strn[i-1] == ')' or strn[i-1] == ']':
#                 if c == ')':
#                     res += '*2'
#                 elif c == ']':
#                     res += '*3'
#             else:
#                 if c == ')':
#                     res += '+2'
#                 elif c == ']':
#                     res += '+3'
#     res = re.sub('[+]+', '+', res)
#     print(res)
#     return eval(res)

# print(solution('(()[[]])([])'))
