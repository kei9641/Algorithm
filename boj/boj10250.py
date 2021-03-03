# 입력
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    
    # 계산
    room, floor = divmod(N, H)
    if not floor:
        floor = H
        room -= 1
    roomNum = floor * 100 + room + 1
    
    # 출력
    print(roomNum)