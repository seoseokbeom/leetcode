def hammingDistance(x: int, y: int):
    x = format(x, '0b')
    y = format(y, '0b')
    mx = max(len(x), len(y))
    zeroes = abs(len(x)-len(y))
    if len(x) > len(y):
        y = '0'*zeroes+y
    else:
        x = '0'*zeroes+x
    cnt = 0
    print(x, y)
    for i in range(len(x)):
        if x[i] != y[i]:
            cnt += 1
    return cnt


print(hammingDistance(1, 4))
