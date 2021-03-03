T = int(input())
for _ in range(T):
    N = int(input())
    case = 0

    def move(n):
        global case
        if n == N:
            case += 1
            return
        elif n > N:
            return
        
        move(n+3)
        move(n+2)
        move(n+1)

    move(0)
    print(case)
