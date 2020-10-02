def solution(arr1, arr2):
    tmp = 0
    arr = []
    res = []
    for i in range(len(arr1)):
        for k in range(len(arr2[0])):
            for j in range(len(arr1[0])):
                tmp += arr1[i][j]*arr2[j][k]
            arr.append(tmp)
            tmp = 0
        res.append(arr)
        arr = []
    return res


print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]]	,
               [[5, 4, 3], [2, 4, 1], [3, 1, 1]]		))
