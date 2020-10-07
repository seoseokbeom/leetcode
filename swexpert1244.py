import sys


def solution(n, cnt):
    arr1 = list(map(lambda e: int(e), list(str(n))))
    arr2 = list(sorted(map(lambda e: int(e), list(str(n))), reverse=True))
    # print(list(arr1), list(arr2))
    res = []
    c = 0
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            c += 1
        if c > 2*cnt:
            arr2[i] = arr1[i]
    return ''.join(map(lambda e: str(e), arr2))

    # strn = str(n)
    # for i in range(cnt):
    #     big = int(strn[i])
    #     idx = -1
    #     for j in range(len(strn)-1, i, -1):
    #         if int(strn[j]) > big:
    #             idx, big = j, int(strn[j])
    #             # print(idx, big)
    #     if idx != -1:
    #         strn = list(strn)
    #         strn[i], strn[idx] = strn[idx], strn[i]
    #         strn = ''.join(strn)
    #         # print(i, strn)
    # return (int(strn))


n = int(input())


for i in range(1, n+1):
    a, b = map(int, input().split())
    ans = solution(a, b)
    print('#{} {}'.format(i, ans))

# print(solution(2737, 1               ))
