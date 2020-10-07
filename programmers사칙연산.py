# def solution(arr, s=0):
#     if len(arr) == 1:
#         return int(arr[0])
#     mx = float('-inf')
#     for i in range(0, len(arr)-2, 2):
#         num = eval(''.join(arr[i:i+3]))
#         mx = max(mx, solution(arr[:i]+[str(num)]+arr[i+3:], s+num))
#     return mx

    # return recursion(arr, 0)


def recursion(arr, sum1):
    if len(arr) == 1:
        return int(arr[0])
    mx = float('-inf')
    for i in range(0, len(arr)-2, 2):
        num = eval(''.join(arr[i:i+3]))
        arr2 = arr[:i]+[str(num)]+arr[i+3:]
        mx = max(mx, recursion(arr2, sum1+num))
    return mx

    #     def solution(arr):
    #     global res
    # res = 0
    # recursion(arr, 0)
    # return res

def solution(arr):
    global res
    res = 0
    recursion(arr, 0)
    return res


def recursion(arr, sum1):
    global res
    if len(arr) == 1:
        res = max(res, int(arr[0]))
        return
    for i in range(0, len(arr)-2, 2):
        num = eval(''.join(arr[i:i+3]))
        arr2 = arr[:i]+[str(num)]+arr[i+3:]
        recursion(arr2, sum1+num)

        def solution(arr):
        global res
    res = 0
    recursion(arr, 0)
    return res

print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))
