sentence = input()
upper_cnt = 0
lower_cnt = 0

for word in sentence:
    if word.isupper():
        upper_cnt += 1
    elif word.islower():
        lower_cnt += 1
print('UPPER CASE {}' . format(upper_cnt))
print('LOWER CASE {}' .format(lower_cnt))
