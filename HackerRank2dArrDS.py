#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(arr):
    mx = float('-inf')
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[0])-1):
            mx = max(mx, getsum(arr, i, j))
    print(mx)
    return mx


def getsum(arr, i, j):
    print(i, j, [arr[x][k] for k in range(j-1, j+2) for x in [i-1, i+1]])
    return arr[i][j]+sum([arr[x][k] for k in range(j-1, j+2) for x in [i-1, i+1]])

# test = [[0 for i in range(6)] for j in range(6)]
# test[0]=[]

# print(hourglassSum())


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
