N = int(input())
visited = [0 for _ in range(N+1)]
case = 0

def attack(x, y, x0, y0):
    if abs(x - x0) == abs(y - y0):
        return True
    return False
    
def put(x):
    global case

    if x > N:
        case += 1
        return

    for y in range(1, N+1):
        if not visited[y]:
            for i in range(1, N+1):
                if visited[i] and attack(x, y, visited[i], i):
                    break
            else:
                visited[y] = x
                put(x + 1)
                visited[y] = 0
put(1)
print(case)