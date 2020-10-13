
from time import time


def solution(N):
    arr = []
    for i in range(2, 10):
        tmp = base(N, i)
        arr.append(tmp)
    mx = arr[0]
    idx = 0
    for i, v in enumerate(arr):
        if v >= mx:
            mx = v
            idx = i
    return [idx+2, mx]


def solution2(N):
    arr = []
    for i in range(3, 10):
        arr.append(base(N, i))
    mx = arr[0]
    idx = 0
    for i, v in enumerate(arr):
        if v >= mx:
            mx = v
            idx = i
    return [idx+3, mx]


def solution3(N):
    idx = 0
    mx = 1
    for i in range(3, 10):
        result = base2(N, i)
        if result >= mx:
            mx, idx = result, i
    return [idx, mx]

    arr.append(base2(N, i))
    mx = arr[0]
    for i, v in enumerate(arr):
        if v >= mx:
            mx = v
            idx = i
    return [idx+3, mx]


def base(N, n):
    arr = []
    while N:
        N, r = divmod(N, n)
        arr.append(r)
    res = 1
    for i, v in enumerate(arr):
        if v != 0:
            res *= v
    # print(arr, res)
    return res


def base2(N, n):
    # arr = []
    res = 1
    while N:
        N, r = divmod(N, n)
        if r != 0:
            res *= r
    return res
    # arr.append(r)
    # res = 1
    # for i, v in enumerate(arr):
    #     if v != 0:
    #         res *= v
    # print(arr, res)


start = time()
for i in range(10, 100000):
    solution3(i)
end = time()
print(end-start)
start = time()
for i in range(10, 100000):
    solution(i)
end = time()
print(end-start)

# if solution(i) != solution2(i) or solution(i) != solution3(i):
# print('FALSE!')
# else:
#     print('True')
# print(i, solution(i), solution2(i))

print(solution3(10))
# print(solution2(10))
# print(solution(999999))
print(solution3(14))
