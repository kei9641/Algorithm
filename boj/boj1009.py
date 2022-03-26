routine = {
    0 : [10],
    1 : [1],
    2 : [2, 4, 8, 6],
    3 : [3, 9, 7, 1],
    4 : [4, 6],
    5 : [5],
    6 : [6],
    7 : [7, 9, 3, 1],
    8 : [8, 4, 2, 6],
    9 : [9, 1]
}

tc = int(input())
for _ in range(tc):
    a, b = map(int, input().split())
    computers = routine[a % 10]

    if (len(computers) == 1):
        print(computers[0])
    else:
        print(computers[(b - 1) % len(computers)])
