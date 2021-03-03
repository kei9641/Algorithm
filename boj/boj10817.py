three_num = list(map(int, input().split()))
three_num.pop(three_num.index(max(three_num)))
print(max(three_num))