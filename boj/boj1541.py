formula = input().split('-')

for i in range(len(formula)):
    sumNum = 0
    for num in formula[i].split('+'):
        sumNum += int(num)
    formula[i] = sumNum

result = int(formula[0])
for j in range(1, len(formula)):
    result -= int(formula[j])

print(result)
    