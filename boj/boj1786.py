import sys

T = sys.stdin.readline().replace("\n", "")
P = sys.stdin.readline().replace("\n", "")

TL = len(T)
PL = len(P)

repeat = [0 for _ in range(PL)]

for i in range(1, PL+1):
    pattern = P[:i]
    for j in range(1, len(pattern)):
        if pattern[:j] == pattern[-j:]:
            repeat[i-1] = j

i, j, n = 0, 0, 0
count = 0
index = []
while i < TL:
    if P[j] == T[i]:
        i += 1
        j += 1
    elif n:
        j = n
    else:
        i += 1
        j = 0
    
    if j == PL:
        if repeat[-1]:
            j = repeat[-1]
        else:
            j = 0
        count += 1
        index.append(i - PL + 1)
    n = repeat[j]
    

print(count)
print(*index)