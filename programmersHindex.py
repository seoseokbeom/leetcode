def solution(citations):
    citations.sort()
    res = binary(citations, 0, len(citations)-1)
    return res


def binary(arr, lo, hi):
    if lo >= hi:
        return hi
    length = len(arr)
    mid = (lo+hi)//2
    if arr[mid] == length-mid:
        return arr[mid]
    if arr[mid] > length-mid:
        hi = mid-1
    else:
        lo = mid+1
    return binary(arr, lo, hi)


print(solution([4, 4, 4]
               ))
