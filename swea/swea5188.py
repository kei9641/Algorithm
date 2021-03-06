def dfs(x, y):
    global route, result
    if x == N-1 and y == N-1:
        route += board[x][y]
        if result > route:
            result = route
    elif x == N-1: # 1
        route += board[x][y]
        dfs(x, y+1)
    elif y == N-1: # 2
        route += board[x][y]
        dfs(x+1, y) 
    else:
        route += board[x][y]
        dfs(x+1, y)
        dfs(x, y+1)
    route -= board[x][y]
   
T = int(input())
for tc in range(T):
    N = int(input())
    board = []
    route = 0
    result = 987654321
    for _ in range(N):
        board.append(list(map(int, input().split())))
    dfs(0, 0)
    print('#{} {}'.format(tc+1, result))