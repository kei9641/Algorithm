# 선언
sugar = 0

# 입력
N = int(input())

# 봉지에 설탕담기
while 1:
    if not N % 5:
        sugar += (N // 5)
        break
    N -= 3
    sugar += 1
    if N < 0:
        sugar = -1
        break
    elif N == 0:
        break

# 출력
print(sugar)