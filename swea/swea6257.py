fruit = ['   apple    ','banana','  melon'] 

result = {fruit[i].strip() : len(fruit[i].strip()) for i in range(len(fruit))}
print(result)