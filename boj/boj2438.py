N = int(input())

for line in range(1, N+1):
    for turn in range(line):
        print('*', end='')
    print()