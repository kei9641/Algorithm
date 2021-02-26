N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

blue, white = 0, 0
def division(x, y, n):
    global blue, white
    color = paper[x][y]
    check = True
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]:
                division(x, y, n//2)
                division(x, y+n//2, n//2)
                division(x+n//2, y, n//2)
                division(x+n//2, y+n//2, n//2)
                check = False
                break
        if not check:
            break
    else:
        if color:
            blue += 1
        else:
            white += 1

division(0, 0, N)
print(white)
print(blue)