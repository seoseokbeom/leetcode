def solution(n):
    cnt = 0
    while n != 1:
        if n % 2 == 1:
            cnt += 1
            n = (n-1)//2
        else:
            n //= 2
    return cnt+1


print(solution(6))
print(solution(5000))
