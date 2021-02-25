N = int(input())
cycle = 0
num = N
while 1:
    cycle += 1
    num = (num % 10) * 10 + ((num // 10) +  (num % 10)) % 10
    if num == N:
        break

print(cycle)