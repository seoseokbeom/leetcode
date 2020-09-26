def solution(n):
    res = ''
    dic = {
        0: 4,
        1: 1,
        2: 2,
        3: 4
    }
    tmp = n-1
    res = ''
    while n:
        if n <= 3:
            res = str(dic[(n-1) % 3])+res
        else:
            res = str(dic[n % 3])+res
        n //= 3
    return res
    # if n%3==0:
    #     res='4'+res
    # elif n%3==1:
    #     res='1'+res
    # else:
    #     res='2'+res


# print(solution(5))
for i in range(1, 11):
    print(solution(i))
