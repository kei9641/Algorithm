def fibonacci(num): 
    if num < 2: 
        return num 
    else: 
        return fibonacci(num-1)+fibonacci(num-2)


fibo = [fibonacci(i) for i in range(1, 11)]
print(fibo)