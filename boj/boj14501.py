N = int(input())
schedule = [[] for _ in range(N+6)]
for S in range(1, N+1):
    T, P = map(int, input().split())
    schedule[S+T-1].append((S, P))

benefit = [0 for _ in range(N+1)]
for day in range(1, N+1):
    max_pay = 0
    for start, pay in schedule[day]:
        max_pay = max(max_pay, pay + benefit[start-1])
    benefit[day] = max(max_pay, benefit[day-1])

print(benefit[N])