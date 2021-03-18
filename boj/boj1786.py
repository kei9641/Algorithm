import sys

T = sys.stdin.readline().replace("\n", "")
P = sys.stdin.readline().replace("\n", "")

TL = len(T)
PL = len(P)

repeat = [0 for _ in range(PL)]

j = 0
for i in range(1, PL):
    while j and P[i] != P[j]:
        j = repeat[j-1]
    if P[i] == P[j]:
        j += 1
        repeat[i] = j

j = 0
count = 0
index = []
for i in range(TL):
    while j and P[j] != T[i]:
        j = repeat[j-1]
    if P[j] == T[i]:
        if j == PL - 1:
            count += 1
            index.append(i - PL + 2)
            j = repeat[j]
        else:
            j += 1

print(count)
print(*index) 