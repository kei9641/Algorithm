# 선언
members = [[] for _ in range(200)]
ageSort = []

# 입력
N = int(input())
for _ in range(N):
    age, name = input().split()
    
    # 나이 순 정렬
    members[int(age)-1].append((int(age), name))
for i in range(200):
    if members[i]:
        ageSort += members[i]

# 출력
for j in range(len(ageSort)):
    print(*ageSort[j])