def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        line = ''
        bin1 = format(arr1[i], 'b').zfill(n)
        bin2 = format(arr2[i], 'b').zfill(n)
        for j in range(n):
            if bin1[j] == '1' or bin2[j] == '1':
                line += '#'
            else:
                line += ' '
        answer.append(line)
    return answer