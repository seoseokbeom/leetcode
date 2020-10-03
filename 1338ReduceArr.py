from collections import Counter
import math


def minSetSize(arr):
    n = len(arr)
    count = Counter(arr)
    count = sorted(list(count.items()), key=lambda x: x[1], reverse=True)
    cnt = 0
    for i, v in enumerate(count):
        cnt += v[1]
        if cnt >= (n/2):
            return i+1


print(minSetSize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
