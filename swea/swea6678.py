sentences = list()
for i in range(3):
    sentence = input()
    if not sentence:
        break
    sentences.append(sentence)

for i in range(len(sentences)):
    print('>> {}' .format(sentences[i].upper()))