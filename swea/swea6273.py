std1, std2, std3 = (90, 80), (85, 75), (90, 100)

total1 = std1[0] + std1[1]
total2 = std2[0] + std2[1]
total3 = std3[0] + std3[1]

aver1 = total1 / 2
aver2 = total2 / 2
aver3 = total3 / 2

print('1번 학생의 총점은 {}점이고, 평균은 {}입니다.'.format(total1, aver1))
print('2번 학생의 총점은 {}점이고, 평균은 {}입니다.'.format(total2, aver2))
print('3번 학생의 총점은 {}점이고, 평균은 {}입니다.'.format(total3, aver3))