def solution(numbers):
    map(lambda x: str(x), numbers)
    numbers.sort(key=lambda a, b: (a+b)-(b+a))
    return numbers


print(solution([6, 10, 2]))
