def solution(n):
    if n == 0:
        return 0
    arr = []
    while n:
        n, r = divmod(n, 3)
        arr.append(str(r))
    tmp = ''.join(arr)
    res = 0
    for i in range(len(tmp)):
        res = res*3+int(tmp[i])
    return res
