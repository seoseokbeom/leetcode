def solution(m, k):
    res = ''
    k += '#'
    l = r = 0
    while l < len(m):
        if k[r] == '#':
            res += m[l:]
            break
        if m[l] == k[r]:
            res = res+m[:l]
            m = m[l+1:]
            l = 0
            r += 1
        else:
            l += 1
    return res


print(solution('dccccccaccccxxxxxxxxxxbdcab', "ab"))
