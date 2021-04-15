import heapq

N, M = map(int, input().split())
connect = [[] for _ in range(N+1)]
dept = [0 for _ in range(N+1)]
problems = []
solve = []

for _ in range(M):
    A, B = map(int, input().split())
    connect[A].append(B)
    dept[B] += 1

for i in range(1, N+1):
    if dept[i] == 0:
        heapq.heappush(problems, i)
        dept[i] -= 1

while problems:
    problem = heapq.heappop(problems)
    solve.append(problem)

    for num in connect[problem]:
        dept[num] -= 1
        
    for j in range(1, N+1):
        if dept[j] == 0:
            heapq.heappush(problems, j)
            dept[j] -= 1

print(*solve)