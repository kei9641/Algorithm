A, B = map(int, input().split())
 
seqList = []
k, cnt = 1, 0

while len(seqList) <= B:
    if k == cnt:
        k += 1
        cnt = 0
        continue
    
    seqList.append(k)
    cnt += 1

print(sum(seqList[A - 1:B]))