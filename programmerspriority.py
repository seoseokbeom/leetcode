def solution(priorities, location):
    arr = []
    for i, v in enumerate(priorities):
        arr.append((v, i))
    for i in range(0, len(priorities)):
        j = i+1
        while j < len(priorities):
            if arr[i][0] < arr[j][0]:
                tmp = arr.pop(i)
                arr.append(tmp)
                j = i
            j += 1
    print(arr)
    for i in range(len(priorities)):
        if arr[i][1] == location:
            return i+1
    # return arr[location][1]


print(solution([2, 1, 3, 2], 2))
