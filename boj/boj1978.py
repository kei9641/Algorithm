'''
소수 찾기 => 에라토스테네스의 체
'''
def primeList(n):
    # 에라토스테네스의 체 초기화
    sieve = [True] * n

    # 최대 약수인 루트n까지 탐색
    m = int(n ** 0.5)

    # 소수의 배수를 체크
    for i in range(2, m + 1):
        # i가 소수인 경우
        if sieve[i] == True:           
            # i이후 i의 배수들을 False 판정
            for j in range(i+i, n, i): 
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]

# 입력
N = int(input())
numbers = list(map(int, input().split()))

# 선언
primeCnt = 0

# N이하의 소수 구하기
primeNum = primeList(max(numbers)+1)

# 소수의 수 찾기
for number in numbers:
    if number in primeNum:
        primeCnt += 1

# 출력
print(primeCnt)