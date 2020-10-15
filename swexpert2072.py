T = int(input())
for i in range(1, T + 1):
    numbers = list(map(int, input().split()))
    odd_nums = [num for num in numbers if num % 2 == 1]
    print("#{} {}".format(i, sum(odd_nums)))
