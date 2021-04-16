after = []
before = list(input())
M = int(input())
for _ in range(M):
    commands = list(input().split())
    if commands[0] == 'L':
        if before:
            after.append(before.pop())
    elif commands[0] == 'D':
        if after:
            before.append(after.pop())
    elif commands[0] == 'B':
        if before:
            before.pop()
    elif commands[0] == 'P':
        before.append(commands[1])

print(''.join(before + list(reversed(after))))
