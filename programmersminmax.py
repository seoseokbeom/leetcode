def solution(s):
    arr = s.split(' ')
    arr = list(map(int, arr))
    arr2 = [min(arr), max(arr)]
    arr2 = [str(i) for i in arr2]
    return ' '.join(arr2)


print(solution('1 2 3 4'))
