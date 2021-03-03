# 이진탐색(재귀)
def binarySearch(a, target, startIdx, endIdx):
    # A에 x가 없는 경우 탈출
    if startIdx > endIdx:
        return False
    # 중간값
    middleIdx = (startIdx + endIdx) // 2
    # 재귀
    if a[middleIdx] > target:
        return binarySearch(a, target, startIdx, middleIdx-1)
    elif a[middleIdx] < target:
        return binarySearch(a, target, middleIdx+1, endIdx)
    # A에 x가 있는 경우 탈출
    else:
        return True

# 입력
N = int(input())
A = list(map(int, input().split()))
M = int(input())
X = list(map(int, input().split()))

# 정렬
A = sorted(A) 

# 출력
for x in X:
    if binarySearch(A, x, 0, N-1):
        print(1)
    else:
        print(0)