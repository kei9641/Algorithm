N = int(input())
A = list(map(int, input().split()))

lcs = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            lcs[i] = max(lcs[i], lcs[j] + 1)

print(max(lcs))
