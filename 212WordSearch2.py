class Solution(object):
    def findWords(self, board, words):
        res = []
        visited = set()
        for word in words:
            for i, row in enumerate(board):
                for j, elem in enumerate(row):
                    if word not in visited and elem == word[0]:
                        self.bfs(board, word, i, j, res, visited)
        return res

    def bfs(self, board, word, i, j, res, visited):
        board_visited = [[False for _ in board[0]] for _ in board]
        board_visited[i][j] = True
        visited_copy = board_visited.copy()
        queue = [[(i, j), visited_copy]]
        direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        cnt = 0
        if(cnt == len(word)-1):
            res.append(word)
            visited.add(word)
            return
        while len(queue) != 0:
            # print(queue)
            tmp = queue.pop()
            pos = tmp[0]
            print(tmp)
            board_visited = tmp[1]
            cnt += 1
            if cnt > len(word)-1:
                return
            for dirct in direction:
                (y, x) = (dirct[0]+pos[0], dirct[1]+pos[1])
                # print(y, x)
                if 0 <= x < len(board[0]) and 0 <= y < len(board):
                    if board[y][x] == word[cnt] and board_visited[y][x] == False:
                        tmp = board_visited.copy()
                        tmp[y][x] = True
                        if(cnt == len(word)-1):
                            print('-----')
                            res.append(word)
                            visited.add(word)
                            return
                        queue.append([(y, x), tmp])


a = Solution()
print(a.findWords(board=[
    ['a', 'a', 'b', 'n'],
    ['a', 'a', 'b', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
],
    words=["aaaa"]
))
