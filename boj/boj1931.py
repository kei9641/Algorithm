N = int(input())
reservation = []
for _ in range(N):
    start, end = map(int, input().split())
    reservation.append((start, end))

reservation.sort(key=lambda x: x[0])
reservation.sort(key=lambda x: x[1])

count = 0
start = 0
for meeting in reservation:
    if start <= meeting[0]:
        start = meeting[1]
        count += 1

print(count)

