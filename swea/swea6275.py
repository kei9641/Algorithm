delete = "aeiou"
sentence = 'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'
result = [i for i in sentence if i not in delete]
print(''.join(result))