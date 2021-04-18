from collections import deque
N = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]

K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = -1

commands = deque()
L = int(input())
for _ in range(L):
    X, C = input().split()
    commands.append([X, C])

def isNotWall(x, y):
    return (0 <= x < N) and (0 <= y < N)

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
n = 0
x, y = 0, 0
length, time = 1, 0

while isNotWall(x, y):
    if board[x][y] == -1:
        length += 1
    if board[x][y] and board[x][y] >= abs(time - length):
        break
    
    board[x][y] = time
    if commands and int(commands[0][0]) == time:
        X, C = commands.popleft()
        if C == 'D':
            n += 1
            if n == 4:
                n -= 4
        else:
            n -= 1
            if n == -1:
                n += 4
    time += 1
    x, y = x + dx[n], y + dy[n]

print(time)