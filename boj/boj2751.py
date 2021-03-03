'''
버블정렬(N^2) : 구현이 쉬움, 비효율적임
선택정렬(N^2) : 버블보단 조금 더 나음
퀵정렬(NlogN) : 기준값(pivot)을 통한 분할
힙정렬(NlogN) : 가장 효율적임, 추가 메모리 불필요
삽입정렬(N) : 엄청 빠름, 성능 편차가 심함
병합정렬(NlogN) : 반으로 분할, 추가 메모리 필요
'''
def mergeSort(arr):
    if len(arr) > 1:
        # 반으로 분할
        middle = len(arr)//2
        leftArr, rightArr = arr[:middle], arr[middle:]

        # 재귀
        mergeSort(leftArr)
        mergeSort(rightArr)
 
        # 선언
        leftIdx, rightIdx = 0, 0
        completeIdx = 0
        
        # 분할된 배열을 정렬
        while leftIdx < len(leftArr) and rightIdx < len(rightArr):
            if leftArr[leftIdx] < rightArr[rightIdx]:
                arr[completeIdx] = leftArr[leftIdx]
                leftIdx += 1
            else:
                arr[completeIdx] = rightArr[rightIdx]
                rightIdx += 1
            # 배열에 정렬된 인덱스
            completeIdx += 1
        
        # 오른쪽 배열을 다 정렬한 경우
        if leftIdx != len(leftArr):
            arr[completeIdx:] = leftArr[leftIdx:]
        # 왼쪽 배열을 다 정렬한 경우
        else:
            arr[completeIdx:] = rightArr[rightIdx:]
    
    # 배열의 원소가 하나면 끝
    return arr

# 선언
mergeList = []

# 입력
N = int(input())
for i in range(N):
    mergeList.append(int(input()))

mergeList = mergeSort(mergeList)
 
# 출력
for j in mergeList:
    print(j)
