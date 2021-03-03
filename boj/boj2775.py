# 선언
apartment = [[0 for _ in range(15)] for _ in range(15)]

# 0층 거주자 수
apartment[0] = list(range(15))

# 전체 거주자 수
for floor in range(1, 15):
    for room in range(1, 15):
        apartment[floor][room] = apartment[floor][room-1] + apartment[floor-1][room]

# 입력
T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    # 출력
    print(apartment[k][n])
