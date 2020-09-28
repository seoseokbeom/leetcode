def solution(n, arr1, arr2):
    return [format(arr1[i] | arr2[i], '0{}b'.format(n)).replace('0', ' ').replace('1', '#') for i in range(n)]


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]
               ))
