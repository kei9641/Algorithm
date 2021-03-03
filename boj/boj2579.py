step = []
N = int(input())
for _ in range(N):
    step.append(int(input()))

point = []

for i in range(N):
    if i == 0:
        point.append(step[0])
    elif i == 1:
        point.append(step[1] + point[0])
    elif i == 2:
        point.append(step[2] + max(step[1], step[0]))
    else:
        point.append(step[i] + max(step[i-1] + point[i-3], point[i-2]))

print(point[-1])