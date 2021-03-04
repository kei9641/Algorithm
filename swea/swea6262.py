word_cnt = {}
words = input()

for word in words:
    word_cnt[word] = words.count(word)

for word, cnt in word_cnt.items():
    print('{},{}' .format(word, cnt))