from collections import Counter


def mostcommon(arr):
    return Counter(arr).most_common()[0][0]


T = int(input())
for i in range(1, T+1):
    input()
    arr = list(map(int, input().split()))
    print('#{} {}'.format(i, mostcommon(arr)))


print(mostcommon([1, 2, 3, 3, 4]))
