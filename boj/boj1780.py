paper = []
count = {
    0: 0, 
    1: 0, 
    -1: 0
}

N = int(input())
for _ in range(N):
    paper.append(list(map(int, input().split())))

def cut(startX, startY, size):
    num = paper[startX][startY]

    if size == 1:
        count[num] += 1
        return

    for i in range(startX, startX + size):
        for j in range(startY, startY + size):
            if paper[i][j] != num:
                n = size//3
                for x in range(startX, startX + size, n):
                    for y in range(startY, startY + size, n):
                        cut(x, y, n)
                return

    count[num] += 1

cut(0, 0, N)

print(count[-1])
print(count[0])
print(count[1])
