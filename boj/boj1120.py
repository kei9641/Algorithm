A, B = input().split()

i = 0
length = len(A)
min_gap = length
while length <= len(B) - i:
    gap = 0
    for j in range(length):
        if A[j] != B[i+j]:
            gap += 1
    min_gap = min(min_gap, gap)
    i += 1

print(min_gap)