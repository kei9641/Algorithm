n = 10
def countdown(x):
    for i in range(x, 0, -1):
        print(i)
        
print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
if(n > 0):
    countdown(n)