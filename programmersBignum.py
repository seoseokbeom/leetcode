def solution(numbers):
    map(lambda x: str(x), numbers)
    numbers.sort()
    return numbers


print(solution([6, 10, 2]))
