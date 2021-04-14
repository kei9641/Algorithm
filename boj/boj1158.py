from collections import deque

N, K = map(int, input().split())
circle = deque()
for sit in range(1, N+1):
    circle.append(sit)

permutation = []
while circle:
    for _ in range(K-1):
        circle.append(circle.popleft())
    permutation.append(circle.popleft())

print('<' + ', '.join(map(str, permutation)) + '>')