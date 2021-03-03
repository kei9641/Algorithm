from collections import deque

# 입력
N = int(input())

# 선언
queue = deque()
queue += list(range(1,N+1))

# 1장이 남을 때까지 반복
while len(queue) > 1:
    # 카드 버리기
    queue.popleft()
    # 카드 밑으로 옮기기
    queue.append(queue.popleft())

# 출력
print(queue[0])