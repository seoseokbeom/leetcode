def solution(prices):
    for i, v in enumerate(prices):
        for j in range(i+1, len(prices)):
            if v > prices[j] or j == len(prices)-1:
                prices[i] = j-i
                break
    prices[len(prices)-1] = 0
    return prices


a = solution([1, 3, - 1, 2, 0, -1, 9])

print(a)
