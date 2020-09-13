def solution(maze):
    direc = 'd' if maze[0][1] else 'r'
    D = {
        'r': (0, 1),
        'l': (0, -1),
        'u': (-1, 0),
        'd': (1, 0)
    }
    start = [0, 0]
    N = len(maze)
    if N == 0:
        return 0

    def turnleft(dir):
        if dir == 'u':
            return 'l'
        elif dir == 'l':
            return 'd'
        elif dir == 'd':
            return 'r'
        elif dir == 'r':
            return 'u'

    def turnright(dir):
        if dir == 'u':
            return 'r'
        elif dir == 'r':
            return 'd'
        elif dir == 'd':
            return 'l'
        elif dir == 'l':
            return 'u'
    answer = 0
    leftdir = direc
    while True:

        leftdir = turnleft(direc)
        if(0 <= start[0]+D[leftdir][0] < N and 0 <= start[1]+D[leftdir][1] < N and maze[start[0]+D[leftdir][0]][start[1]+D[leftdir][1]] == 0):
            direc = leftdir
        elif(start[0]+D[direc][0] < 0 or start[0]+D[direc][0] >= N or start[1]+D[direc][1] < 0 or start[1]+D[direc][1] >= N or maze[start[0]+D[direc][0]][start[1]+D[direc][1]] == 1):
            rightdir = turnright(direc)
            direc = rightdir
        a, b = start[0] + D[direc][0], start[1]+D[direc][1]
        if 0 <= a < N and 0 <= b < N and maze[a][b] != 1:
            start = [a, b]
            answer += 1
        if start[0] == len(maze)-1 and start[1] == len(maze[0])-1:
            break

    return answer
    # print(start, answer, direc)
    # print(start[0]+D[direc][0], start[1]+D[direc][1])
    # print(start[0]+D[leftdir][0], start[1]+D[leftdir][1])

    # print('----1', start[0]+D[leftdir][0], start[1]+D[leftdir][1])
    # print('----', start[0]+D[direc][0], start[1]+D[direc][1])


# print(solution([[0, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0], [1, 0, 1, 0]]	))
# print(solution([[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [
#       0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]	))
# print(solution([[0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [
#       0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0]]		))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 0], [
      1, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0]]			))
