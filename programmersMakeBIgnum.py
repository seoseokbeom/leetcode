def solution(number, k):
    global arr
    arr = []
    recursion(number, 0, '', k)
    print(arr)
    return max(arr)


def recursion(num, i, s, k):
    if k == 0:
        global arr
        arr.append(eval(s+num[i:]))
        return
    if i >= len(num):
        return
    recursion(num, i+1, s, k-1)
    recursion(num, i+1, num[i]+s, k)


print(solution('1231234', 3))
