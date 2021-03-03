video = []
N = int(input())
for _ in range(N):
    video.append(list(map(int, input())))

def quadTree(startX, startY, size):
    num = video[startX][startY]

    for i in range(startX, startX + size):
        for j in range(startY, startY + size):
            if video[i][j] != num:
                n = size//2
                return '(' + quadTree(startX, startY, n) + quadTree(startX, startY + n, n) + quadTree(startX + n, startY, n) + quadTree(startX + n, startY + n, n) + ')'
    return str(num)

print(quadTree(0, 0, N))