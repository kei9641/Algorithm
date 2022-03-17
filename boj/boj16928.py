import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = dict()
for _ in range(N + M):
    x, y = map(int, input().split())
    board[x] = y


score = [(1, 0)] 
minTurn = [100] * 101 
minTurn[1] = 0 

while score: 
    position, roll = score.pop() 
    
    if position >= 100: 
        if minTurn[100] > roll: 
            minTurn[100] = roll
        continue 
    
    for dice in range(1, 7): 
        if board.get(position + dice): 
            if minTurn[board.get(position + dice)] > roll + 1: 
                minTurn[board.get(position + dice)] = roll + 1 
                score.append((board.get(position + dice), roll + 1)) 
        else: 
            if position + dice < 101 and minTurn[position + dice] > roll + 1: 
                score.append((position + dice, roll + 1)) 
                minTurn[position + dice] = roll + 1 
                
print(minTurn[100])
