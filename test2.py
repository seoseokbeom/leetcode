def solution(arr):
    global ones
    global zeros
    ones = sum(sum(row) for row in arr)
    zeros = len(arr)*len(arr[0])-ones
    rec(arr)
    return [zeros, ones]


def rec(arr):
    if len(arr) == 0 or len(arr) % 2 == 1:
        return
    global ones
    global zeros
    if sum(sum(row) for row in arr) == 0:
        zeros = zeros - len(arr)*len(arr[0])+1
    elif sum(sum(row) for row in arr) == len(arr)*len(arr[0]):
        ones = ones-len(arr)*len(arr[0])+1
    else:
        lenrow = len(arr)//2
        for i, row in enumerate(arr):
            arr[i] = [arr[i][:lenrow], arr[i][lenrow:]]
        rec([arr[i][0] for i in range(lenrow)])
        rec([arr[i+lenrow][0] for i in range(lenrow)])
        rec([arr[i][1] for i in range(lenrow)])
        rec([arr[i+lenrow][1] for i in range(lenrow)])