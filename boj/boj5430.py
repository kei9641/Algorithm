T = int(input())
for _ in range(T):
    arr = []
    p = input()
    n = int(input())
    numbers = input()[1:-1]
    if numbers:
        arr += list(numbers.split(','))
    
    p.replace('RR', '')
    l, r, rvs = 0, 0, False

    for commend in p:
        if commend == 'R':
            rvs = not rvs
        elif commend == 'D':
            if rvs:
                r += 1
            else:
                l += 1
    
    if l + r > len(arr):
        print('error')
    else:
        arr = arr[l:len(arr)-r]
        if rvs:
            arr.reverse()
        print('[{}]'.format(','.join(arr)))
