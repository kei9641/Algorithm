i = str(input())

if((i >= "a") and (i <= "z")): #i.islower()
    a = ord(i)
    b = ord(i) - ord("a") + ord("A")
    j = chr(b)
    '''
    ord() chr()
    temp = lower(i)
    print(temp)
'''
    print("%s(ASCII: %d) => %s(ASCII: %d)" %(i, a, j, b)) 
elif((i >= "A") and (i <= "Z")):
    a = ord(i)
    b = ord(i) - ord("A") + ord("a")
    j = chr(b)
    print("%s(ASCII: %d) => %s(ASCII: %d)" %(i, a, j, b)) 
else:
    print(i)