words = [[] for _ in range(50)]
dictionary = []

N = int(input())
for _ in range(N):
  word = input()
  words[len(word)-1].append(word)

for length in range(50):
  words[length] = list(set(words[length]))
  words[length].sort()

for i in range(50):
  if words[i] != []:
    dictionary += words[i]
  
for sort_word in dictionary:
  print(sort_word)