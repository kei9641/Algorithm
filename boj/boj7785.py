from collections import defaultdict

log = defaultdict(bool)
n = int(input())
for _ in range(n):
    name, state = input().split()
    if state == 'enter':
        log[name] = True
    else:
        log[name] = False

enter = []
for staff, isWork in log.items():
    if isWork:
        enter.append(staff)

enter.sort(reverse=True)
for name in enter:
    print(name)