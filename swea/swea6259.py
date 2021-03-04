sentence = input()
letter_cnt = 0
digit_cnt = 0

for word in sentence:
    if (('a' <= word <= 'z') or ('A' <= word <= 'Z')):
        letter_cnt += 1
    elif ('0' <= word <= '9'):
        digit_cnt += 1
print('LETTERS {}' .format(letter_cnt))
print('DIGITS {}' .format(digit_cnt))