def solution(a):
    global res
    res = set()
    global dp
    dp = set()
    rec(a, 1, 0)
    return len(res)


def rec(arr, i, mark):
    global res
    global dp
    if (tuple(arr), i, mark) in dp:
        return
    else:
        dp.add((tuple(arr), i, mark))
    if(len(arr) == 1):
        res.add(arr[0])
        return
    if(i >= len(arr)):
        return
    if arr[i-1] <= arr[i]:
        rec(arr[0:i]+arr[i+1:], 1, mark)
        if mark == 0:
            rec(arr[0:i-1]+arr[i:], 1, 1)
    else:
        rec(arr[0:i-1]+arr[i:], 1, mark)
        if mark == 0:
            rec(arr[0:i]+arr[i+1:], 1, 1)
    rec(arr, i+1, mark)


# print(solution([1,2,3,4]))
# print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]	))
