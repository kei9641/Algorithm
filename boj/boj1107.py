N = int(input())
M = int(input())
destroys = []
if M:
    destroys += list(input().split())


push = abs(N - 100)
for channel in range(1000001):
    for num in str(channel):
        if num in destroys:
            break
    else:
        push = min(push, len(str(channel)) + abs(N - channel))

print(push)