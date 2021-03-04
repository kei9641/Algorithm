score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
a = 0
i = 0
while i<len(score):
    b = score.pop(i)
    if(b>=80):
        a = a + b
print(a)