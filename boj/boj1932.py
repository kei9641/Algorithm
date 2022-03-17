triangle = []

n = int(input())
for _ in range(n):
    triangle.append(list(map(int, input().split())))

for line in range(1, n):
    for col in range(len(triangle[line])):
        if (col == 0):
            triangle[line][col] += triangle[line - 1][col]
        elif (col == line):
            triangle[line][col] += triangle[line - 1][col - 1]
        else:
            triangle[line][col] += max(triangle[line - 1][col], triangle[line - 1][col - 1])

print(max(triangle[-1]))

