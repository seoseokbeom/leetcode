class Solution(object):
    def numRookCaptures(self, board):
        pos = ()
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v == 'R':
                    pos = (i, j)
                    break
        cnt = 0
        tmp = pos
        (i, j) = tmp
        j = tmp[1]
        # print(i, j)
        while j > 0:
            j -= 1
            if board[i][j] == '.':
                continue
            elif board[i][j] == 'B':
                break
            else:
                cnt += 1
                break
        j = tmp[1]
        while j < len(board[0])-1:
            # print(i, j)
            j += 1
            if board[i][j] == 'p':
                cnt += 1
                break
            elif board[i][j] == 'B':
                break

        (i, j) = tmp
        while i > 0:
            i -= 1
            if board[i][j] == '.':
                continue
            elif board[i][j] == 'B':
                break
            else:
                cnt += 1
                break

        (i, j) = tmp

        while i < len(board[0])-1:
            print(i, j)
            i += 1
            if board[i][j] == 'p':
                cnt += 1
                break
            elif board[i][j] == 'B':
                break
        # while j <
        # print(pos)
        return cnt


a = Solution()
print(a.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]))
