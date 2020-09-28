def generateParenthesis(n):
    global res
    res = []
    rec(n, 0, 0, '')
    return res


def rec(n, l, r, save):
    if n == l == r:
        global res
        res.append(save)
        return
    if l < 3:
        rec(n, l+1, r, save+'(')
    if l > r and r < 3:
        rec(n, l, r+1, save+')')


print(generateParenthesis(3))
