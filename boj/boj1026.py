N = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())))

S = 0
for i in range(N):
    S += A[i] * B[i]

print(S)