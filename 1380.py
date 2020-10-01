def luckyNumbers(matrix):
    vis = set()
    # print(zip(*matrix))
    # testi for i in zip(*matrix)
    for i, row in enumerate(matrix):
        mn = min(row)
        for j, v in enumerate(row):
            if v == mn:
                vis.add((i, j))
    res = []
    for j in range(len(matrix[0])):
        mx = max(row[j] for row in matrix)
        for i in range(len(matrix)):
            if matrix[i][j] == mx and (i, j) in vis:
                res.append(matrix[i][j])
    return res


print(luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
# print(luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
# print(luckyNumbers([[7, 8], [1, 2]]))
