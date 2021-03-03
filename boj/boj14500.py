paper = []
N, M = map(int, input().split())
for _ in range(N):
    paper.append(list(map(int, input().split())))

# dr, dl, rd, ld, vert, hori
plusX = [[0, -1, 1, 2, 2, 1, 0], [-1, 0, 2, 2, 1], [0, 2, 0], [0, 2], [], []]
plusY = [[1, 0, 2, 1, 0, -1, -1], [0, 1, 0, -1, -2], [2, 1, -1], [1, -1], [], []]

sumX = [[1, 1, 0], [1, 1, 0], [1, 0, 0], [1, 0, 0], [3, 2, 1, 0], [0, 0, 0, 0]]
sumY = [[1, 0, 0], [-1, 0, 0], [1, 1, 0], [-1, -1, 0], [0, 0, 0, 0], [3, 2, 1, 0]]

def isNotWall(x, y):
    return (0 <= x < N) and (0 <= y < M)

def block(x, y, k):
    blockSum = 0
    if isNotWall(x+sumX[k][0], y+sumY[k][0]):
        for n in range(len(plusX[k])):
            xn, yn = x + plusX[k][n], y + plusY[k][n]
            if isNotWall(xn, yn) and blockSum < paper[xn][yn]:
                blockSum = paper[xn][yn]
        if k >= 4 or blockSum:
            for m in range(len(sumX[k])):
                xm, ym = x + sumX[k][m], y + sumY[k][m]
                blockSum += paper[xm][ym]
    return blockSum

maxSum = 0
for i in range(N):
    for j in range(M):
        for k in range(6):
            tetromino = block(i, j, k)
            if maxSum < tetromino:
                maxSum = tetromino

print(maxSum)